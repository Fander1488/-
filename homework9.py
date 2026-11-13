import colorama
from colorama import Fore, Back, Style, init

print("--- ІНТРОСПЕКЦІЯ MODULE: COLORAMA ---")
print(f"Доступні атрибути та модулі всередині colorama (dir):")
print(dir(colorama))
print("\n" + "="*50 + "\n")

print("--- ІНТРОСПЕКЦІЯ КЛАСУ Fore (Кольори тексту) ---")
print(dir(Fore))

print("\n" + "="*50 + "\n")

init(autoreset=True)

print("--- ДЕМОНСТРАЦІЯ РОБОТИ ---")

print(Fore.RED + "Цей текст виведено червоним кольором.")
print(Fore.GREEN + "Цей текст виведено зеленим кольором.")
print(Fore.BLUE + "Цей текст виведено синім кольором.")

print(Back.YELLOW + Fore.BLACK + "Текст із чорним шрифтом на жовтому фоні.")

print(Style.BRIGHT + Fore.CYAN + "Яскравий блакитний текст (Бридкий/Жирний стиль).")
print(Style.DIM + "Цей текст має зменшену яскравість (DIM).")

print("Цей текст знову має стандартний колір завдяки autoreset=True.")