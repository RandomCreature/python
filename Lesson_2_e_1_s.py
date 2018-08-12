# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 3. киви
# 4. арбуз
# Подсказка: воспользоваться методом .format()

# Способ_1

lst = ['Pear', 'Quince', 'Persimmon', 'Pomegranate']
for i in range(len(lst)):
    print(i, lst[i])

# Способ_2

for i, word in enumerate(lst):
    print(str(i+1)+'.'+'{:>14}'.format(word))

# Способ_3

for i, word in enumerate(lst):
    print(i+1,'.', word.rjust(12))

# Способ_4

for i, word in enumerate(lst, 1):
    print(f'{i}. {word.rjust(13)}')
