import colorama
import inspect
from colorama import Fore, Back, Style, init

print("=== ІНТРОСПЕКЦІЯ МОДУЛЯ COLORAMA ===")
print("Список усіх об'єктів у модулі colorama:")
print(dir(colorama))
print("-" * 50)

print("=== КЛАС Fore (кольори тексту) ===")
print("Атрибути та методи:")
print(dir(Fore))
print("-" * 50)

print("=== ДОСЛІДЖЕННЯ ФУНКЦІЇ init ЗА ДОПОМОГОЮ inspect ===")
print("Сигнатура функції init:", inspect.signature(init))
print("Вихідний код функції init:")
print(inspect.getsource(init))
print("-" * 50)

init(autoreset=True)  # Автоматично скидає кольори після кожного print

print(Fore.RED + "Цей текст виведено червоним кольором (Fore.RED).")
print(Back.YELLOW + Fore.BLACK + "Текст на жовтому фоні (Back.YELLOW).")
print(Style.BRIGHT + Fore.GREEN + "Яскравий зелений текст (Style.BRIGHT).")
print("Цей рядок знову стандартний, завдяки autoreset=True.")