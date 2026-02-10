def input_employee_salary_data():
    name = input("Nhap ten nhan vien: ")
    working_hours_per_day = float(input("Nhap so gio lam viec moi ngay: "))
    working_days_per_month = int(input("Nhap so ngay lam viec trong thang: "))
    hourly_wage = float(input("Nhap luong moi gio: "))

    return name, working_hours_per_day, working_days_per_month, hourly_wage
