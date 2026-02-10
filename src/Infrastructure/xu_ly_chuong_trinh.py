from src.Domain.salary_algorithm import SalaryAlgorithm

class ProcessingProgram:
    def process(
        self,
        name: str,
        working_hours_per_day: float,
        working_days_per_month: int,
        hourly_wage: float
    ) -> dict:

        algorithm = SalaryAlgorithm()
        total_salary = algorithm.calculate_total_salary(
            working_hours_per_day,
            working_days_per_month,
            hourly_wage
        )

        return {
            "name": name,
            "total_salary": total_salary
        }
