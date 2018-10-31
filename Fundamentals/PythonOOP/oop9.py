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

    def fullname(self):
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

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        else:
            return True

    ##representation of object
    ## debugging logging
    def __repr__(self):
        ##trying to return a string that can use to re-create object
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    ##readable represenation of an object
    ## for end users
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None :
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(' --> ', emp.getFullName())
    #pass

print(Employee.num_of_employees)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)



dev_1 = Developer("Chamin", "Nalinda", 5000, 'Python')
dev_2 = Developer("Thilina", "Gamalath", 6000, 'Java')
dev_3 = Developer("Saman", "Alvitigla", 5200, 'Lisp')


mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(1+2)
print('a'+'b')

print("\n \n")

print(emp_1)

print(repr(emp_1))
print(str(emp_1))

print("\n \n")
print(int.__add__(1,3))
print(str.__add__('Chamin', ' Nalinda'))

print(emp_1 + emp_2)


print(len('test'))
print('test'.__len__())


print(len(emp_1))
