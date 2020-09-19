import pytest

from software_testing.exercises.exercise4.ir_calculator import IRCalculator


@pytest.mark.parametrize(
    "salary, target_ir", [(1000, 0.0), (1500, 75.0), (2500, 250.0), (3500, 475.0),],
)
def test_calculate_ir(salary, target_ir):
    # act
    output_ir = IRCalculator.calculate_ir(salary)

    # assert
    assert target_ir == output_ir
