class IncomeTaxCalculator:
    def __init__(self, monthly_income: float):
        self.monthly_income = monthly_income

    @property
    def total_tax(self) -> float:
        return (
            self.tax_fifth_track
            + self.tax_fourth_track
            + self.tax_third_track
            + self.tax_second_track
        )

    @property
    def tax_fifth_track(self) -> float:
        return 0.275 * max(self.monthly_income - 4664.69, 0)

    @property
    def tax_fourth_track(self) -> float:
        return 0.225 * max(min(self.monthly_income, 4664.68) - 3751.06, 0)

    @property
    def tax_third_track(self) -> float:
        return 0.15 * max(min(self.monthly_income, 3751.05) - 2826.66, 0)

    @property
    def tax_second_track(self) -> float:
        return 0.075 * max(min(self.monthly_income, 2826.65) - 1903.99, 0)
