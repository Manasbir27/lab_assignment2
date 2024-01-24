class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def display_table(self):
        for employee in self.employees:
            print(f"Employee ID: {employee.employee_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

    def sort_table(self, key):
        if key == 1:
            self.employees.sort(key=lambda x: x.age)
        elif key == 2:
            self.employees.sort(key=lambda x: x.name)
        elif key == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting key")

if __name__ == "__main__":
    employee1 = Employee("161E90", "Ramu", 35, 59000)
    employee2 = Employee("171E22", "Tejas", 30, 82100)
    employee3 = Employee("171G55", "Abhi", 25, 100000)
    employee4 = Employee("152K46", "Jaya", 32, 85000)

    employees_list = [employee1, employee2, employee3, employee4]

    employee_table = EmployeeTable(employees_list)

    print("Before Sorting:")
    employee_table.display_table()

    sorting_key = int(input("Enter sorting parameter (1. Age, 2. Name, 3. Salary): "))
    employee_table.sort_table(sorting_key)

    print("\nAfter Sorting:")
    employee_table.display_table()
