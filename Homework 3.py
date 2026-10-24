n = int(input("Введіть число n: "))

start_even = n if n % 2 == 0 else n - 1

print(f"Парні числа від {n} до 1 у зворотному порядку:")
for i in range(start_even, 1, -2):
    print(i, end=" ")
print()
