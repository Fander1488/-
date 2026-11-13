filename = input("Введіть шлях до файлу (наприклад, text.txt): ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print("\n--- Вміст файлу ---")
        print(content)
except FileNotFoundError:
    print(f"Помилка: Файл за шляхом '{filename}' не існує!")
except Exception as e:
    print(f"Сталася непередбачувана помилка: {e}")