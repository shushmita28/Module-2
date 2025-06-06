# Single Inheritance
Define the Base class Employee
class Employee:
    def __init__(self, name,employee_id , salary):
        """
        Initializse the Employee class with employee details such as name, ID,and salary.id
        """
        self.name = name 
        self.employee_id = employee_id
        self.salary = salary
    def display_details(self):
        """
        Displays the employee's details.
        """
        return f"Employee Name: {self.name}\nEmployee ID: {self.employee_id}\nSalary: ₹{self.salary:.2f}"

# Task 2 : Define the Derived class Manager

class Manager(Employee):
    def __init__(Self, name, employee_id, salary,team_size):
        """
        Intitalize the Manager class , which inherits from Employee and the team size attrbute.AttributeError
        """
        super().__init__(name, employee_id, salary)
        Self.team_size = team_size

    def display_details(self):
        """
        Displays the manager's details, including team size.'
        """
        employee_details = super().display_details()
        return f"{employee_details}\nTeam Size: {self.team_size}"

# Task 3: Instantiate objects frome Base and Derived Classes 
if __name__ == "__main__":
    employee = Employee("Employee1", "E001", 50000)
    manager = Manager("Manager", "M456", 80000, 0)
    print("Employee Details:")
    print(employee.display_details())
    print("\nManager Details:")
    print(manager.display_details())

# Multiple Inheritance
 Define the Base class person

class Person:
    def __init__(self, name):
        """
        Intitialzes the Person class with the person's name .self
        """
        self.name = name 
    def greet(self):
        """
        Returns a greeting message with the person's name. 
        """
        return f"Hello. I 'm {self.name}"

# Task 2
class Employee:
    def __init__(self, employee_id):
        """
        Initializess the emlpoyee class with employee 's ID.
        """
        self.employee_id = employee_id
    def get_employee_id (self):
        """
        Returnh the employee ID.
        """
        return self.employee_id
    
# Task 3
class Manager(Person, Employee):
    def __init__(self, name, employee_id):
        """"
        Initializes the Manager class, which inherits from both person and Employee 
        """
        Person.__init__(self, name)
        Employee.__init__(self, employee_id)

# # Task 4
if __name__ == "__main__" :
    manager = Manager("Ramar Bose", "E12345")
    print(manager.greet())
    print(f"Employee ID: {manager.get_employee_id()}")

# Hierarchical Inheritance
Task 1
class person:
    def __init__(self, name, age):
        """
        Initialize the Person class with common personal details such as name and age.age
        """
        self.name = name 
        self.name = age
    def disply_personal_details(self):
        """
#             Displays the person's name and age.
#             """
        return f"Name : {self.name}, Age {self.agr}"
    
# Task 2
class Employee(person):
    def __init__(self,name,age,employee_id,salary):
        """
        Initialize the Employee class, which inherits from Person and adds employee details.
        """
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary
    def disply_employee_details(self):
        """
        Disply employee-specifice such as employee ID  and salary.
        """
        personal_details = self.display_personal_details()
        return f"{personal_details}, Employee ID: {self.employee_id}, Salary: ₹{self.salary:.2f}"

# Task 3
class Manager(Employee):
    def __init__(self, name, age, emplyee_id, salary, department, team_size):
        """
        Initializes the Manager class, which inherits from Employee and add manager-specifice details.
        """
        super().__init__(name, age,emplyee_id, salary)
        self.departement = department
        self.team_size = team_size
    def disply_employee_details(self):
        """
        Displays manager-specifice details along with inherited personal and employee details.
        """
        employee_details = self.disply_employee_details()
        return f"{employee_details}, Department: {self.departement}, Team size: {self.team_size}"
    
# Task 4
if __name__ == "__main__":
    manager = Manager("Ramar Bose", 45, "M12345", 95000, "Sales", 10)
    print("Manager Details:")
    print(manager.disply_employee_details())

