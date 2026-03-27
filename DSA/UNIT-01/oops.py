
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, emp_id, name, basic_salary):
        self._emp_id = emp_id         
        self._name = name              
        self._basic_salary = basic_salary
    @abstractmethod
    def calculate_salary(self):
        pass    

class PermanentEmployee(Employee):
    def calculate_salary(self):
        hra = self._basic_salary * 0.20     
        da = self._basic_salary * 0.10      
        total_salary = self._basic_salary + hra + da
        return total_salary


# ---------------------------------------------------------
# STEP 4: Create ContractEmployee class
# Also inherits Employee class
# ---------------------------------------------------------
class ContractEmployee(Employee):

    # -----------------------------------------------------
    # Constructor with extra parameter hours_worked
    # super() calls parent class constructor
    # -----------------------------------------------------
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name, hourly_rate)
        self._hours_worked = hours_worked   # Protected variable

    # -----------------------------------------------------
    # Overridden method for salary calculation
    # Demonstrates RUNTIME POLYMORPHISM
    # -----------------------------------------------------
    def calculate_salary(self):
        return self._basic_salary * self._hours_worked


# ---------------------------------------------------------
# STEP 5: PayrollSystem class
# Handles multiple employees
# ---------------------------------------------------------
class PayrollSystem:

    # -----------------------------------------------------
    # Constructor initializes empty employee list
    # -----------------------------------------------------
    def __init__(self):
        self.employee_list = []   # List to store employee objects

    # -----------------------------------------------------
    # Method to add employee object to list
    # -----------------------------------------------------
    def add_employee(self, employee):
        self.employee_list.append(employee)

    # -----------------------------------------------------
    # Method to display salary details
    # -----------------------------------------------------
    def show_payroll(self):
        for emp in self.employee_list:
            print("Employee ID   :", emp._emp_id)
            print("Employee Name :", emp._name)
            print("Salary        :", emp.calculate_salary())
            print("-------------------------------")


# ---------------------------------------------------------
# STEP 6: MAIN PROGRAM
# Object creation and method calling
# ---------------------------------------------------------

# Create PayrollSystem object
payroll = PayrollSystem()

# Create PermanentEmployee object
emp1 = PermanentEmployee(101, "Rahul", 30000)

# Create ContractEmployee object
emp2 = ContractEmployee(102, "Amit", 500, 40)

# Add employees to payroll system
payroll.add_employee(emp1)
payroll.add_employee(emp2)

# Display payroll details
payroll.show_payroll()




