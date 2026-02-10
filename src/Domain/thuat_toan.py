class SalaryAlgorithm:
    def calculate_total_salary(
        self,
        working_hours_per_day: float,
        working_days_per_month: int,
        hourly_wage: float
    ) -> float:
        total_hours = working_hours_per_day * working_days_per_month
        total_salary = total_hours * hourly_wage
        return total_salary
