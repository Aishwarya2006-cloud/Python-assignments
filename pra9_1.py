"""
Create a class Employee inherits it into another class Manager. Add methods to get input & print information of employees. Consider the attributes name, age, salary, address etc. Process the information of 10 managers.
"""


class Employee:
    def getData(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.address = input("Enter Address: ")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    pass


managers = []

for i in range(10):
    print("\nEnter details of Manager", i+1)
    m = Manager()
    m.getData()
    managers.append(m)

print("\nManager Information")
for i in managers:
    print("\n--- Manager Details ---")
    i.display()