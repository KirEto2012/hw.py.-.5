# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

a = int(input('введите первое число:'))
b = int(input('введите второе число:'))

from modul1 import function_that_returns_sum_of_two_numbers

print(function_that_returns_sum_of_two_numbers(a,b))