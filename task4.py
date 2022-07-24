# 3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]

numberN = int(input('enter N: '))

def find_simple_multiplier (num):
    my_list = []
    i = 2
    while num !=1:
        if num % i == 0:
            my_list.append(i)
            num = num // i
        else: 
            i = i+1
    return my_list

answer = find_simple_multiplier(numberN)

print(list(set(answer)))