# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

path = 'mama2.txt'
data = open(path, 'r')
substring = data.read().split()

new_list = []
for words in substring:
    if words.isalpha():
        new_list.append(words)

data.close()

print (' '.join(new_list))