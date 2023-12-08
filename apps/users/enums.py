from enum import Enum


class RegEx(Enum):
    PASSWORD = (
        r'/^((?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9]).{6,})\S$/',
        [
            'Checks that a password has a minimum of 6 characters,'
            ' at least 1 uppercase letter,'
            ' 1 lowercase letter,'
            ' and 1 number with no spaces.'
        ]
    )
    NAME = (
        ' ^[a-zA-Z]{2, 100}$ ',
        'only letters min 2 max 100'
    )

    def __init__(self, pattern: str, msg: str | list(str)):
        self.pattern = pattern
        self.msg = msg
