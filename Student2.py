class Student:
    grade = 6
    name = "Python"

    def introduction(self):
        print("Hello i am a student")

    def details(self):
        print("I study in grade ", self.grade)
        print("My name is" , self.grade)


student = Student()
student.introduction()
student.details()