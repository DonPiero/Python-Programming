class Employee:
    def __init__(self, name, employeeId, salary):
        self.name = name
        self.employeeId = employeeId
        self.salary = salary

    def displayInfo(self):
        print(f"Name: {self.name}.")
        print(f"Employee ID: {self.employeeId}.")
        print(f"Salary: {self.salary}.")

class Manager(Employee):
    def __init__(self, name, employeeId, salary, department):
        super().__init__(name, employeeId, salary)
        self.department = department

    def promoteEmployee(self, employee):
        print(f"{employee.name} has been promoted in the {self.department} department.")

class Engineer(Employee):
    def __init__(self, name, employeeId, salary, programmingLanguage):
        super().__init__(name, employeeId, salary)
        self.programmingLanguage = programmingLanguage

    def code(self):
        print(f"{self.name} is coding in {self.programmingLanguage}.")

class Salesperson(Employee):
    def __init__(self, name, employeeId, salary, salesQuota):
        super().__init__(name, employeeId, salary)
        self.salesQuota = salesQuota

    def make_sale(self, amount):
        if amount >= self.salesQuota:
            print(f"{self.name} made a sale of ${amount}. Quota achieved!")
        else:
            print(f"{self.name} made a sale of ${amount}. Quota not achieved.")

manager = Manager("Mike Tyson", 10, 10000, "Sales")
engineer = Engineer("Jon Jones", 20, 8000, "Python")
salesperson = Salesperson("Connor McGregor", 30, 6000, 2000)

manager.displayInfo()
manager.promoteEmployee(engineer)

engineer.displayInfo()
engineer.code()

salesperson.displayInfo()
salesperson.make_sale(4000)
