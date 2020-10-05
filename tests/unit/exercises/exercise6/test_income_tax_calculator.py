import pytest

from software_testing.exercises.exercise6.income_tax_calculator import (
    IncomeTaxCalculator,
)


@pytest.mark.parametrize(
    "salary, target_tax",
    [
        (1903.98, 0),
        (2500, 44.70075),
        (3500, 170.20050000000003),
        (4500, 376.3695000000001),
        (10000, 1880.6327500000004),
    ],
)
def test_calculate_ir(salary, target_tax):
    # arrange
    calculator = IncomeTaxCalculator(salary)

    # act
    output_tax = calculator.total_tax

    # assert
    print(output_tax)
    assert target_tax == output_tax
