from src.Domain.algorithm import Algorithm
from src.Presentation.nhap_thong_tin import EmployeeSalaryCalculationFormula
from src.Application.kiem_tra_du_lieu_dau_vao import CheckInputData
from src.Presentation.in_thong_tin_kiem_tra_dau_vao import printinformationcheck
from src.Infrastructure.xu_ly_chuong_trinh import ProcessingData
from src.Presentation.in_ket_qua import PrintResult
from src.tests.unitests import TestProgram


def main():
    # ======================
    # 1. THUẬT TOÁN
    # ======================
    algorithm = Algorithm()

    # ======================
    # 2. NHẬP DỮ LIỆU
    # ======================
    name, hours_per_day, days_per_month, hourly_wage = (
        EmployeeSalaryCalculationFormula()
    )

    # ======================
    # 3. KIỂM TRA DỮ LIỆU
    # ======================
    is_valid = CheckInputData(
        name,
        hours_per_day,
        days_per_month,
        hourly_wage
    )

    # ======================
    # 4. IN THÔNG TIN KIỂM TRA
    # ======================
    printinformationcheck(is_valid)

    if not is_valid:
        return

    # ======================
    # 5. XỬ LÝ CHƯƠNG TRÌNH
    # ======================
    processor = ProcessingData(algorithm)
    result = processor.process(
        name,
        hours_per_day,
        days_per_month,
        hourly_wage
    )

    # ======================
    # 6. IN KẾT QUẢ
    # ======================
    PrintResult(result)


if __name__ == "__main__":
    # ======================
    # 7. TEST
    # ======================
    TestProgram()
    main()
