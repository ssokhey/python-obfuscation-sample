from src.math_func import func_multiply, func_add, func_sqrt
from src.text_func import func_greeting, func_completion

name = "User"

a = 7
b = 3

def logic():
    print(func_greeting(name))
    x = func_add(a, b)
    y = func_multiply(a, b)
    z = func_sqrt(a + b)
    print(func_completion(a,b, x, y, z))
    return z
