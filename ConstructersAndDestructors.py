class Employee:
    def __init__(self):
        print("The employeee has been created")

    def __del__(self):
        print("employee has been deleted")

obj = Employee()
del obj