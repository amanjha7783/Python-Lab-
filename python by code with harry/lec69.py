class Employee:
  name = "John Doe"  # instance variable
  company_name = "Tech Solutions Inc."

  def show(self):
    print(f"Welcome to {self.company_name}and employee name is {self.name}")

  @classmethod
  def change_company_name(cls, new_name):
    cls.company_name = new_name

# Creating an instance of Employee
emp = Employee()  
emp.name = "Aman jha"
emp.show()  # Output: Welcome to Tech Solutions Inc.
emp.change_company_name("tesla")
emp.show()
print(Employee.company_name)
