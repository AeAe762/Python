# Задача N 25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

s = 'a a a b a c b b d d'.split()
r = ''

for i, letter in enumerate((s)):
    if s[:i].count(letter)<1:
        r+=letter+' '
    else:
        r+=f'{letter}_{s[:i].count(letter)} '
print(r)



s = 'a a a b a c b b d'.split()
r = ''
for i in range(len(s)):
    if s[0:i:].count(s[i]) == 0:
        r += s[i]
    else:
        r += f'{s[i]}_{s[0:i].count(s[i])}'
    print(s[0:i], r)
print(r)