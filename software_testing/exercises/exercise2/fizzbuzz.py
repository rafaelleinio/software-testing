"""Fizzbuzz Module."""

from typing import List


class FizzBuzz:
    """Fizzbuzz class definition.

    Attributes:
        n: number of elements for the sequence.

    """

    def __init__(self, n: int):
        self.n = n

    @staticmethod
    def _is_multiple_of_3(x) -> bool:
        return x % 3 == 0

    @staticmethod
    def _is_multiple_of_5(x) -> bool:
        return x % 5 == 0

    @staticmethod
    def _get_element(x):
        is_multiple_of_3 = FizzBuzz._is_multiple_of_3(x)
        is_multiple_of_5 = FizzBuzz._is_multiple_of_5(x)

        if is_multiple_of_3:
            value = "Fizz"
            if is_multiple_of_5:
                return value + "Buzz"
            return value
        if is_multiple_of_5:
            return "Buzz"
        return str(x)

    def get_sequence(self) -> List[str]:
        """Get Fizz Buzz sequence."""
        return [self._get_element(x) for x in range(1, self.n + 1)]
