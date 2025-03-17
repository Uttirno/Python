i = input("Enter the robots name: ")

class Robot:
    def __init__(self, name):
        self.name = name


robot = Robot(i)
print("Hello i am a robot and my name is ", robot.name)
