"""Triangle Module."""


class TriangleTypes:
    """Triangle types enumerator."""

    EQUILATERAL = "Equilateral"
    ISOSCELES = "Isosceles"
    SCALENE = "Scalene"


class Triangle:
    """Basic triangle definition.

    Attributes:
        side_a: first side of the triangle.
        side_b: second side of the triangle.
        side_c: third side of the triangle
        type: type of the triangle

    """

    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self._validate_triagle()

    def _validate_triagle(self):
        a_validation = self.side_a >= self.side_b + self.side_c
        b_validation = self.side_b >= self.side_a + self.side_c
        c_validation = self.side_c >= self.side_a + self.side_b
        if a_validation or b_validation or c_validation:
            raise ValueError("Defined sides can't build a valid triangle.")

    @property
    def type(self) -> str:
        """Get the triangle type.

        Returns:
            Name of the triangle type.

        """
        distinct_sides = len({self.side_a, self.side_b, self.side_c})
        if distinct_sides == 3:
            return TriangleTypes.SCALENE

        if distinct_sides == 2:
            return TriangleTypes.ISOSCELES

        if distinct_sides == 1:
            return TriangleTypes.EQUILATERAL
