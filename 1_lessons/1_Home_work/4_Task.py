# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов
# сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два
# раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# x - сделал Петя и Серёжа
# (x + x) * 2 = 4x - сделала Катя
# x + 4x + x = s
# 6x = s
# x = s/6
s = int(input('Введите количество журавлей: '))
p = s/6 #сделал Петя
k = s/6 * 4 #сделала Катя
c = s/6  #сделал Серёжа
print('Петя сделал -', int(p),';', 'Катя сделала -', int(k),';', 'Сережа сделал -', int(c))