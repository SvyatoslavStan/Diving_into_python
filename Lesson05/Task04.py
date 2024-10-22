# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

def even_numbers_generator(limit):
    for number in range(0, limit + 1, 2):
        if number % 2 == 0 and sum(int(digit) for digit in str(number)) != 8:
            yield number

print(list(even_numbers_generator(80)))