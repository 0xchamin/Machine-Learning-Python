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

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

print(Employee.num_of_employees)
emp_1 = Employee("Chamin", "Nalinda", 5000)
emp_2 = Employee("Thilina", "Gamalath", 6000)

emp_str_1 = 'John-Doe-7000'
emp_str_2 = 'Steve-Smith-3000'
emp_str_3 = 'Jane-Doe-9000'

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.email)
