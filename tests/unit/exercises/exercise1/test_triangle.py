import pytest

from software_testing.exercises.exercise1.triangle import Triangle, TriangleTypes


class TestTriangle:
    @pytest.mark.parametrize(
        "side_a, side_b, side_c", [(1, 3, 2.5), (1.5, 1.5, 2.9), (3, 3, 3)]
    )
    def test_valid_triangle(self, side_a, side_b, side_c):
        # arrange
        triangle_types = [
            TriangleTypes.EQUILATERAL,
            TriangleTypes.ISOSCELES,
            TriangleTypes.SCALENE,
        ]

        # act
        triangle = Triangle(side_a, side_b, side_c)

        # assert
        assert triangle.type in triangle_types

    @pytest.mark.parametrize(
        "side_a, side_b, side_c", [(1, 2, 3), (1.5, 1.5, 3), (1, 2, 3.00001)]
    )
    def test_invalid_triangle(self, side_a, side_b, side_c):
        # act and assert
        with pytest.raises(ValueError):
            Triangle(side_a, side_b, side_c)

    @pytest.mark.parametrize(
        "side_a, side_b, side_c, target_type",
        [
            (1, 3, 2.5, TriangleTypes.SCALENE),
            (1.5, 1.5, 2.9, TriangleTypes.ISOSCELES),
            (3, 3, 3, TriangleTypes.EQUILATERAL),
        ],
    )
    def test_type(self, side_a, side_b, side_c, target_type):
        # arrange
        triangle = Triangle(side_a, side_b, side_c)

        # act
        result_type = triangle.type

        # assert
        assert target_type == result_type
