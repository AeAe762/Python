# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите
# минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите количество монеток: '))
count0 = 0  # считает количество 0
count1 = 0  # считает количество 1

for i in range(n):
    q = int(input())
    if q == 0:
        count0 += 1
    else:
        count1 += 1
if count0 > count1:
    print(count1)
else:
    print(count0)
