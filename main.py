from application.salary import calculate_salary
from application.db.people import Employee
from datetime import date

current_date = date.today()

if __name__ == '__main__':
    print(f'Сегодня: {current_date}')
    employee = Employee('Ivan', 'Ivanov')
    employee.get_employees()

    calculate_salary()
