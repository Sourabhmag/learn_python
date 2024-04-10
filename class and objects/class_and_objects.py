class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


emp = Employee(10, "Sourabh")
print("id:", emp.id, "\nName:", emp.name)

del emp.id
# This will give you an error as id is deleted
print("id:", emp.id, "\nName:", emp.name)

del emp
# this will give you an error as emp is deleted
print(emp)
