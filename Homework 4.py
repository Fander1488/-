n = int(input("Введіть число n для обчислення факторіалу: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Факторіал числа {n} ({n}!) дорівнює: {factorial}")
