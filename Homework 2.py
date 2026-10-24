start = int(input("Введіть початкове число (з): "))
end = int(input("Введіть кінцеве число (по): "))

print(f"Числа від {start} до {end}:")
for i in range(start, end + 1):
    print(i, end=" ")
print()
