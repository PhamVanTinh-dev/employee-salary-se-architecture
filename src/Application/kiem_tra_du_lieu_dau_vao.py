def check_input_data(
    name: str,
    working_hours_per_day: float,
    working_days_per_month: int,
    hourly_wage: float
) -> bool:

    if not name.isalpha():
        return False

    if working_hours_per_day <= 0:
        return False

    if working_days_per_month <= 0:
        return False

    if hourly_wage <= 0:
        return False

    return True
