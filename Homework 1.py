import random

secret_number = random.randint(1, 10)
attempts = 3

print("Комп'ютер загадав число від 1 до 10. У вас є 3 спроби, щоб вгадати його.")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Спроба {attempt}. Введіть ваше число: "))

    if guess == secret_number:
        print("Вітаємо! Ви вгадали число!")
        break
    elif guess > secret_number:
        print("Менше")
    else:
        print("Більше")
else:
    print(f"На жаль, спроби закінчилися. Загадане число було: {secret_number}")
