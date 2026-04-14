from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, emp_id, name, basic_salary):
        self._emp_id = emp_id          
        self._name = name              
        self._basic_salary = basic_salary
    
    @abstractmethod
    def calculate_salary(self):
        pass    

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
class ContractEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name, hourly_rate)
        self._hours_worked = hours_worked 
        return self._basic_salary * self._hours_worked
class PayrollSystem:
    def __init__(self):
        self.employee_list = []   
    def add_employee(self, employee):
        self.employee_list.append(employee)
    def show_payroll(self):
        for emp in self.employee_list:
            print("Employee ID   :", emp._emp_id)
            print("Employee Name :", emp._name)
            print("Salary        :", emp.calculate_salary())
            print("-------------------------------")
payroll = PayrollSystem()

emp1 = PermanentEmployee(101, "Rahul", 30000)
emp2 = ContractEmployee(102, "Amit", 500, 40)
payroll.add_employee(emp1)
payroll.add_employee(emp2)
payroll.show_payroll()




