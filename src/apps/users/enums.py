from apps.core.utils import BaseEnumerate


class GenderEnum(BaseEnumerate):
    MALE = 1
    FEMALE = 2

    values = {
        MALE: 'm',
        FEMALE: 'f',
    }
