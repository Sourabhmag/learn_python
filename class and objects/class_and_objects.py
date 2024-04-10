class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


emp = Employee(10, "Sourabh")
print("id:", emp.id, "\nName:", emp.name)
