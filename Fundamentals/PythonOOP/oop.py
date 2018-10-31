class Employee:
    def __ini__(self, fist, last, pay):
        ##self is the instance
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@campany.com'
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

#Instance variables
emp_1.first = 'Chamin'
emp_1.last = 'Nalinda'
emp_1.email = 'chamin.nalinda@gmail.com'
emp_1.pay = 5000

emp_2.first = 'Chamara'
emp_2.last = 'Silvar'
emp_2.email = 'chamara.silva@gmail.com'
emp_2.pay = 6000


print(emp_1.first)
print(emp_2.last)
