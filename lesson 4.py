class Parent:
    def __init__(self, eye_color, surname):
        self.eye_color = eye_color
        self.surname = surname

    def info(self):
        print(f"My surname is {self.surname}. I have {self.eye_color} eyes.")

    def cooking(self):
        print("Cook delicious meat 🥩🧑‍🍳")

class Son(Parent):
    def programming(self):
        print("I'm a python developer 💻🧑‍💻")

print("==================Father================")
mark = Parent("gray", "Smith")
mark.info()
mark.cooking()
print("==================Son====================")
john = Son("gray","Smith" )
john.info()
john.programming()
john.cooking()