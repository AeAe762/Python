# Задача No19. Решение в группах
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения списка или список задан изначально.

list_1 = [1, 2, 3, 4, 5]
k = int(input('Введите число сдвига: '))
list_2 = []
for i in range(len(list_1)):
    list_2.append(list_1[i-k])
print((list_2))
list_1 = [int(input('Введите число сдвига: '))]

# a = [1, 2, 3, 4, 5]
# k = 3
# i = 0
# while i < k:
#     poped = a.pop()
#     a.insert(0, poped)
#     i += 1
# print(a)