from employee_interface import EmployeeInterface
from employee import Employee

class EmployeeProxy(EmployeeInterface):
    def __init__(self):
        self._employee = Employee()
    
    def create(self, user:str, name:str, age:int):
        if user == "ADMIN":
            self._employee.create(name, age)
        else:
            raise Exception("Not an Admin")
    
    def get(self, user:str, name:str):
        if user == "ADMIN":
            self._employee.get(name)
        else:
            raise Exception("Not an Admin")
        
    def delete(self, user:str, name:str):
        if user == "ADMIN":
            self._employee.delete(name)
        else:
            raise Exception("Not an Admin")