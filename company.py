from employee import Employee

class Company:
    def __init__(self, name):
        self.name = name
        self.employess = []

def add_employees(self, new_employee):
    self.employees.append(new_employee)

def display_employees(self):
    print('Current Employees:')
    for i in self.employees:
        print(i.fname, i.lname)
    print('-------------------')

def main():
    my_company = Company()

    employee1 = Employee('Big', 'Billy', 160000)
    my_company.add_employee(employee1)
    employee2 = Employee('Jeff', 'Free', 100000)
    my_company.add_employee(employee2)
    employee3 = Employee('Mr.', 'Hangman', 175000)
    my_company.add_employee(employee3)

    my_company.display_employees()
