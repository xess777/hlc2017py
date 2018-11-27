class BaseEnumerate:
    """Базовый класс для создания перечислений."""
    values = {}

    @classmethod
    def get_choices(cls):
        return list(cls.values.items())
