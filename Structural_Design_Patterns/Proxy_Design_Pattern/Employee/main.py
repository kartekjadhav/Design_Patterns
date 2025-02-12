from employee_proxy import EmployeeProxy


emp = EmployeeProxy()
emp.create("ADMIN", "Shady", 25)
emp.create("ADMIN", "Sid", 23)
emp.create("ADMIN", "Om", 20)
emp.get("ADMIN", "Shady")
emp.delete("ADMIN", "Sid")