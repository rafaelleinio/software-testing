import pytest

from software_testing.exercises.exercise3.is_valid import is_valid


@pytest.mark.parametrize(
    "exp, target",
    [
        ("abc123", True),
        ("1abc", False),
        ("a bc", False),
        ("", False),
        ("abcdefg", False),
        (123, False),
    ],
)
def test_is_valid(exp, target):
    # act
    result = is_valid(exp)

    # assert
    assert target == result
