# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

import os
os.system('cls')

def Power(a, b):
    if b == 0: 
        return 1
    elif b > 0:
        return a * Power(a, b - 1)
    else:
        return 1/(a * Power(a, (-1) * (b + 1)))
  
A = float(input("Введите число A: "))
B = int(input("Введите число B: "))
if A == 0 and B == 0:
    print('Недопустимый формат ввода чисел.')
else:
    print(f'Число {A} в степени {B} равно {Power(A, B)}')
