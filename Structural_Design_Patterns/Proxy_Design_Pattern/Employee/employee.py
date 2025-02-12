from employee_interface import EmployeeInterface

class Employee:
    def create(self, name:str, age:int):
        print(f"Record for {name} with {age} created")
    
    def get(self, name:str):
        print(f"Record for {name} name is fetched")
    
    def delete(self, name:str):
        print(f"Record for {name} name deleted")