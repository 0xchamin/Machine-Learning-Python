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

print(Employee.num_of_employees)
emp_1 = Employee("Chamin", "Nalinda", 5000)
emp_2 = Employee("Thilina", "Gamalath", 6000)

print(emp_1.pay)
emp_1.apply_raise()

print(emp_1.pay)

##check namespace of instance
print(emp_1.__dict__)

##check namespace of class
print(Employee.__dict__)

print(Employee.num_of_employees)

print(emp_1.num_of_employees)
print(emp_2.num_of_employees)
