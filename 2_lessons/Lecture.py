# list_1 = []
# for i in range (1, 11):
#     list_1.append(i)
# print(list_1)

# from random import randint # генерирует случайные числа
# lst = [randint(1, 10) for i in range(10)]
# #print(lst)
#
# list_1 = [i for i in range(1, 101)]
# print(list_1)

# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# # print(dictionary)
# for item in dictionary:
#     print(item)

from random import randint
n_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
print(n_set)
m_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
print(m_set)
s_set = (n_set.intersection(m_set))
print(*s_set)

