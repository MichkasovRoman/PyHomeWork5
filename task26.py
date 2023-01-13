# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

import os
os.system('cls')

def Power(a, b):
    i = 0
    power = 1
    if b >= 0:
        while i < b:
            power = a * Power(a, i)
            i = i + 1
    if b < 0:
        while i < (-1) * b:
            power = 1 / (a * Power(a, i))
            i = i + 1
    return power

A = float(input("Введите число A: "))
B = int(input("Введите число B: "))
print(f'Число {A} в степени {B} равно {Power(A, B)}')
