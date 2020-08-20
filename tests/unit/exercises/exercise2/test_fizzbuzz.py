import pytest

from software_testing.exercises.exercise2.fizzbuzz import FizzBuzz


class TestFizzBuzz:
    @pytest.mark.parametrize("x", [3, 6, 9, 12, 99])
    def test__is_multiple_of_3(self, x):
        # assert
        assert FizzBuzz._is_multiple_of_3(x)

    @pytest.mark.parametrize("x", [5, 10, 15, 20, 150])
    def test__is_multiple_of_5(self, x):
        # assert
        assert FizzBuzz._is_multiple_of_5(x)

    @pytest.mark.parametrize(
        "n, target_sequence",
        [
            (3, ["1", "2", "Fizz"]),
            (5, ["1", "2", "Fizz", "4", "Buzz"]),
            (
                15,
                [
                    "1",
                    "2",
                    "Fizz",
                    "4",
                    "Buzz",
                    "6",
                    "7",
                    "8",
                    "9",
                    "10",
                    "11",
                    "12",
                    "13",
                    "14",
                    "FizzBuzz",
                ],
            ),
        ],
    )
    def test_type(self, n, target_sequence):
        # arrange
        fizzbuzz = FizzBuzz(n=n)

        # act
        result_sequence = fizzbuzz.get_sequence()

        # assert
        assert result_sequence == target_sequence
