# Погружение в Python (семинары)
# Задание 1. Удаление дубликатов из списка
# Дан список повторяющихся элементов. Вернуть список с дублирующимися
# элементами. В результирующем списке не должно быть дубликатов.
# Подсказка № 1
# Для решения задачи вам нужно найти элементы, которые повторяются в списке.
# Подумайте о том, как можно определить, что элемент повторяется.
# Подсказка № 2
# Метод count позволяет узнать, сколько раз элемент встречается в списке.
# Используйте его, чтобы определить, является ли элемент дублирующимся.

elements = [1, 2, 2, 3, 4, 4, 4, 5, 5]

duplicates = []

for x in elements:

    if elements.count(x) > 1 and x not in duplicates:
        duplicates.append(x)
print(duplicates)