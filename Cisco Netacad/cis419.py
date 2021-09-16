#decomposition example

class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return (self.pay * 12)


class Employee:
    hi=100#just for another example
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.obj_salary = Salary(self.pay) #object of salary class instantiated here #decomposition

    def annual_salary(self):
        return "Total: " + str(self.obj_salary.get_total() + self.bonus)


obj_emp = Employee(600, 500)
print(obj_emp.annual_salary())
print(obj_emp.hi)
print(Employee.hi)

