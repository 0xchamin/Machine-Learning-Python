class Employee:
    #class variable
    raise_amount = 1.04
    num_of_employees = 0

    ##instance variable
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        #number should be same across all objects
        Employee.num_of_employees += 1

    def getFullName(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


print(Employee.num_of_employees)
emp_1 = Employee("Chamin", "Nalinda", 5000)
emp_2 = Employee("Thilina", "Gamalath", 6000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
emp_1.raise_amount = 1.05
print(emp_2.raise_amount)
print(emp_1.raise_amount)

Employee.set_raise_amt(1.06)
print("\n \n ***** \n \n ")
print(Employee.raise_amount)
print(emp_1.raise_amount)
emp_1.raise_amount = 1.05
print(emp_2.raise_amount)
print(emp_1.raise_amount)
