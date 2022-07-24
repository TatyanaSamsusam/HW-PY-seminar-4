# 2- Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#  Посмотрели, что такое множество? Вот здесь его не используйте.

import random

random_list = [random.randint(1,21) for i in range(10)]
print(random_list)

def choose_unique (some_list):
    unique_list = []
    for i in some_list:
        if i in unique_list:
            continue
        else: 
            unique_list.append(i)
    return unique_list

print(choose_unique(random_list))
