import random


class Robot:
    def __init__(self, name):
        self.name = name
        self.battery = 100

    def say_hello(self):
        current_batteries = self.battery // 20
        print(f"Привіт! Я робот {self.name}. Мій заряд: {self.battery}% ({current_batteries} 🔋)")


class CleanerRobot(Robot):
    def clean(self):
        if self.battery >= 20:
            self.battery -= 20
            used_batteries = (100 - self.battery) // 20

            print(f"Робот {self.name} починає прибирання... 🧹")
            print(f"Використано батарейок від початку: {used_batteries} 🔋")
        else:
            print(f"Робот {self.name} не може прибирати, заряд занизький! ❌")


vally = CleanerRobot("Vally")

vally.say_hello()

random_cleans = random.randint(1, 5)
print(f"\n🎲 Заплановано прибирань на сьогодні: {random_cleans}\n" + "-" * 40)

for i in range(random_cleans):
    print(f"Прибирання №{i + 1}:")
    vally.clean()
    print("-" * 40)

vally.say_hello()
