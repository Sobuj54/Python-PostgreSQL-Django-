from menu import Menu

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        for employee in self.employees:
            print(f"name:{employee.name} phone:{employee.phone} email:{employee.email} address:{employee.address} designation:{employee.designation} salary:{employee.salary}")
