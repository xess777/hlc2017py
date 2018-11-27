from apps.core.utils import BaseEnumerate


class MarkEnum(BaseEnumerate):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    values = {
        ZERO: '0',
        ONE: '1',
        TWO: '2',
        THREE: '3',
        FOUR: '4',
        FIVE: '5',
    }
