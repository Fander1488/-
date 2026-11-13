import math

module_name = "math"
function_name = "sqrt"

try:
    if hasattr(math, function_name):
        func = getattr(math, function_name)
        result = func(16)
        print(f"Результат виконання функції {function_name}(16): {result}")
    else:
        raise AttributeError(f"Функцію '{function_name}' не знайдено в модулі '{module_name}'.")

except AttributeError as e:
    print(f"Помилка атрибута: {e}")
except Exception as e:
    print(f"Інша помилка: {e}")