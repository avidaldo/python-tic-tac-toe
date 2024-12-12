from enum import Enum

class Symbol(Enum):
    HUMAN = 'O'
    AI = 'X'

    def __str__(self):
        return self.value