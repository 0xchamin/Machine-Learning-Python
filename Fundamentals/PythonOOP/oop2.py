class Employee:
    #instance variables 
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@campany.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee("Chamin", "Nalinda", 5000)
emp_2 = Employee("Thilina", "Gamalath", 6000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())


print(Employee.fullname(emp_1))## have to pass the instance
