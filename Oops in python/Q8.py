class employee:
    def __init__(self, role,department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self):
        print(f"My role is {self.role} in company")
        print(f"My department is {self.department} in company")
        print(f"My salary is {self.salary} in company")

class Engineer(employee):
    def __init__(self, name, age ):
        super().__init__("Engineer", "IT", "75,000")

# e1 = employee("Manager", "CSE ", "1 ,00,000")
# e1.show_details()

engg1 = Engineer("Elon musk", 40)
engg1.show_details()