# 26 возведение чисел в степень
def exponentiation_of_numbers(a, b):
    if b == 0:
        return 1
    return a * exponentiation_of_numbers(a, b - 1)
# 28 функция, которая возвращает сумму двух чисел
def function_that_returns_sum_of_two_numbers(a,b):
    if b == 0:
        return a
    else:
        return function_that_returns_sum_of_two_numbers(a + 1, b - 1)