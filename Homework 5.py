score = int(input("Введіть кількість балів, яку отримав студент: "))

if score >= 90:
    print("Оцінка: Відмінно (A)")
elif score >= 75:
    print("Оцінка: Добре (B/C)")
elif score >= 60:
    print("Оцінка: Задовільно (D/E)")
else:
    print("Оцінка: Незадовільно (F)")
