import random

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skill = 1
        self.money = 100

    def study(self):
        if self.money >= 20:
            self.skill += 1
            self.money -= 20
            print("studying . . . (+1 skill, -20 money)")
        else:
            print("No money to study! Need to work.")
            self.work()

    def chill(self):
        self.skill = max(0.0, self.skill - 0.5)
        spent_money = random.randint(5, 15)
        self.money = max(0, self.money - spent_money)
        print(f"chilling . . . (-0.5 skill, -{spent_money} money)")

    def work(self):
        self.money += 50
        print("working . . . (+50 money)")

    def info(self):
        print(f"My name is {self.name}. I'm {self.age} years old.")
        print(f"Skills: {self.skill}")
        print(f"Money: {self.money}")
        print("-" * 30)

alex = Student(name="alex", age=15)
alex.info()

for day in range(366):
    choice = random.randint(0, 2)
    if choice == 0:
        alex.chill()
    elif choice == 1:
        alex.study()
    else:
        alex.work()

alex.age += 1
print("\n=== FINAL RESULT AFTER 366 DAYS ===")
alex.info()
