from src.Infrastructure.processing_program import ProcessingProgram

def test_salary_calculation():
    processor = ProcessingProgram()

    result = processor.process(
        name="TINH",
        working_hours_per_day=8,
        working_days_per_month=22,
        hourly_wage=50000
    )

    assert result["total_salary"] == 8 * 22 * 50000
