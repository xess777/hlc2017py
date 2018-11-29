"""Скрипт загрузки данных в БД из zip архива.

Пример запуска скрипта:
$ python manage.py runscript load_data

"""

import json
import logging
import os
from typing import Iterator, Tuple, Union
from zipfile import ZipFile

from django.conf import settings

from apps.locations.models import Location
from apps.users.models import User
from apps.visits.models import Visit


def iterate_zip_files(zip_file_path: str) -> Iterator[Tuple[str, str]]:
    """Генератор возвращающий имя файла с содержимым из zip архива.

    Args:
        zip_file_path: Путь до zip архива.

    Yields:
        (str, str): Имя файла и содержимое.

    Raises:
        FileNotFoundError: Если файл архива не найден.

    """
    with ZipFile(zip_file_path) as zip_file:
        for file_name in zip_file.namelist():
            with zip_file.open(file_name) as _file:
                yield file_name, _file.read()


def parse_json(json_data: str) -> Union[dict, None]:
    """Парсит данные json.

    Args:
        json_data: Данные json.

    Returns:
        dict|None: Словарь с данными из json в случае
            успешного парсинга, иначе None.

    """
    try:
        data = json.loads(json_data)
    except json.JSONDecodeError:
        data = None

    return data


class BaseDataLoader:
    """Базовый класс загрузчика данных в БД.

    Note:
        В классах потомков нужно обязательно переопределить model.

    Attributes:
        data: Словарь с данными для загрузки.

    """
    # Используемая модель для загрузки данных.
    # Переопределяется в наследниках.
    model = None

    def __init__(self, data: dict) -> None:
        """Конструктор.

        Args:
            data: Словарь с данными для загрузки.

        """
        self.data = data

    @staticmethod
    def prepare_params(params: dict) -> dict:
        """Вовзращает обработанный набор параметров.

        Note:
            Переопределяется в потомках, по умолчанию возвращает
            необработанные параметры.

        Args:
            params: Словарь с параметрами.

        Returns:
            Обработанный словарь с параметрами.

        """
        return params

    def load(self) -> None:
        """Загружает данные в БД для соответствующей модели.
        """
        assert self.model is not None

        params_list = next(iter(self.data.values()))
        rows = (
            self.model(**self.prepare_params(params)) for params in params_list
        )
        self.model.objects.bulk_create(rows)


class UserDataLoader(BaseDataLoader):
    """Загрузчик данных модели User.
    """
    model = User


class LocationDataLoader(BaseDataLoader):
    """Загрузчик данных модели Location.
    """
    model = Location


class VisitDataLoader(BaseDataLoader):
    """Загрузчик данных модели Visit.
    """
    model = Visit

    @staticmethod
    def prepare_params(params: dict) -> dict:
        """Вовзращает обработанный набор параметров для модели Visit.

        Args:
            params: Словарь с параметрами.

        Returns:
            Обработанный словарь с параметрами.

        """
        # Приведем наименования FK к формату ORM.
        params['location_id'] = params.pop('location')
        params['user_id'] = params.pop('user')

        return params


def get_data_loader(filename: str) -> Union['BaseDataLoader', None]:
    """Возвращает класс загрузчика данных по имени файла.

    Args:
        filename: имя файла с данными json.

    Returns:
        Класс загрузчика данных, либо None, если загрузчик не найден.

    """
    # Соответсвие маски имени файла к классу загрузчика.
    mapper = {
        'users': UserDataLoader,
        'locations': LocationDataLoader,
        'visits': VisitDataLoader,
    }

    result = None
    for mask, loader in mapper.items():
        if filename.startswith(mask):
            result = loader
            break

    return result


def run(*args) -> None:
    """Скрипт загрузки данных в БД из zip архива.

    Запуск скрипта:
    $ python manage.py runscript load_data

    """
    logger = logging.getLogger()

    if not os.path.isfile(settings.DATA_FILE):
        logger.error(f'Файл {settings.DATA_FILE} не найден.')
        return

    for filename, json_data in iterate_zip_files(settings.DATA_FILE):
        loader = get_data_loader(filename)
        if loader is None:
            continue

        data = parse_json(json_data)
        if data is None:
            logger.error(f'Ошибка парсинга JSON файла {filename}.')
            continue

        loader(data).load()
