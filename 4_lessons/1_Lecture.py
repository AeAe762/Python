# def f(x):
#     return x ** 2
#
#
# # print(f(2))
#
# def math(op, x):
#     print(op(x))
#
#
# print('math(f, 10) ')
# math(f, 10)
# print()
#
#
# # Пример
# def calc2(x):
#     return x * 10
#
#
# def math(op, x):  # op — операция, воспринимаем её как отдельную функцию
#     print(op(x))
#
#
# print('math(calc2, 10)')
# math(calc2, 10)  # 100
# print()
#
#
# # Пример умножение через lambda
# def calc_2(op, a, b):
#     print(op(a, b))
#
#
# print(f"calc_2(lambda x,y: x * y, 5,4):")
# calc_2(lambda x, y: x * y, 5, 4)
# print()
#
#
# # Пример умножение
# def mylt(x, y):
#     return x * y
#
#
# def calc(op, a, b):
#     print(op(a, b))
#
#
# print('calc(mylt, 4, 5)')
# calc(mylt, 4, 5)
# print()


# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38 Получить: [(2, 4), (8, 64), (38, 1444)]


# # Решение № 1
# print('Решение 1')
# list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
# list_2 = []
# for i in range(len(list_1)): # for i in list_1:
#     if list_1[i] % 2 == 0: # if i % 2 == 0:
#         list_2.append((list_1[i], list_1[i]**2)) # list_2.append((i, i**2))
# print(list_2)
#
# Решение 2
# print('Решение 2')
# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]

# data = ['1', '2', '3', '5', '8', '15', '23', '38']
# res = select(int, data)
# print(f'res = {res} ')
# res = where(lambda x: x % 2 == 0, res)
# print(res) # [2, 8, 38]
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)

# Решение № 3 с использованием функции map()

# def where(f, col):
#     return [x for x in col if f(x)]
#
#
# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res2 = where(lambda x: x % 2 == 0, res)
# res3 = list(map(lambda x: (x, x ** 2), res2))
# print(res3)  # [(2, 4), (8, 64), (38, 1444)]


# Функция filter()

# data = [x for x in range(10)]
# res = list(filter(lambda x: x % 2 == 0, data))
# print(res) # [0, 2, 4, 6, 8]
#
# set = [1, 2, 3]
# print(type(set))
# set2 = {x for x in set}
# print(type(set2))
# print(set2)






