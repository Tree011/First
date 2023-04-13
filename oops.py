class employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def get_salary(self,salary):
        self.salary=salary
        print(f'my salary is {self.salary}')

    def set_name(self,name):
        self.name=name
        print(f'new name added,{self.name}')



emp= employee('rohan',234)
print(emp.name)
print(emp.salary)
emp.get_salary(2323)
emp.set_name('avi')