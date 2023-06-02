# # Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах


# n = int(input('Количество элементов первого множества : '))
# my_set = set()
# for i in range(n):
#     my_set.add(input())
# print('Множество 1:', my_set)

# m = int(input('Количество элементов второго множества : '))
# you_set = set()
# for i in range(n):
#     you_set.add(input())
# print('Множество 2:', you_set)

# if my_set.intersection(you_set):
#     our = my_set.intersection(you_set)
#     print(f'Эти цифры находятся в обоих множествах : {sorted(our)}')
# else:
#     print('пересечения множеств не найденно!')



from random import randint
list_1 = list(randint(1, 5) for i in range(int(input('Введите кол-во кустов: '))))
print(list_1)
a = int(input('Введите № куста: '))
res = 0
if a == 1:
    res = list_1[0] + list_1[1] + list_1[-1]
elif a == len(list_1):
    res = list_1[-2] + list_1[-1] + list_1[0]
else:
    res = list_1[a-1] + list_1[a-2] + list_1[a]
print(res, 'ягод')