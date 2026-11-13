user_input = input("Введіть ціле число: ")

try:
    number = int(user_input)
    print(f"Успішно конвертовано! Ви ввели число: {number}")
except ValueError:
    print("Помилка: Введені дані не є цілим числом!")