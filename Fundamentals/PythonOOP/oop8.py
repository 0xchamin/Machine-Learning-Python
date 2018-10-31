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

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        else:
            return True


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
dev_1 = Developer("Chamin", "Nalinda", 5000, 'Python')
dev_2 = Developer("Thilina", "Gamalath", 6000, 'Java')
dev_3 = Developer("Saman", "Alvitigla", 5200, 'Lisp')


mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
