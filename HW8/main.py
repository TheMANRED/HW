from datetime import date
from decimal import Decimal
from classes import Employee

john = Employee(name="John", start=date(2022, 10, 11), rate=Decimal("11"), taxes=10)
alex = Employee(name="Alex", start=date(2021, 5, 6), rate=Decimal("11"), taxes=10)
ksenia = Employee(name="Ksenia", start=date(2019, 10, 29), rate=Decimal("11"), taxes=10)
valeriy = Employee(name="Valeriy", start=date(2020, 1, 3), rate=Decimal("11"), taxes=10)
vera = Employee(name="Vera", start=date(2020, 6, 5), rate=Decimal("11"), taxes=10)
suzanna = Employee(name="Suzanna", start=date(2021, 11, 11), rate=Decimal("11"), taxes=10)
gleb = Employee(name="Gleb", start=date(2022, 2, 23), rate=Decimal("11"), taxes=10)

# ---------------------------------------------------------------------------------------------------------------------

Employee.show_table()

for emp in Employee.employees:
    emp.update_rate(emp.rate + 2)

Employee.show_table()
