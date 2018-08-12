# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

# Способ_1

import random
lst_r = range(1,7)
lst_m = []
for i in lst_r:
    x = random.randint(5,27)
    if x%2 == 1:
        lst_m.append(x*2)
    elif x%2 == 0:
        lst_m.append(x/4)
    else:
        print()
print(lst_m)
print()

# Способ_2
lst = [var1 + var2 for var1 in '127' if var1 != '0' for var2 in '459' if var2 != '1']
lst_n = []
print('Изначальный список',lst)
for y in lst:
    if float(y)%2 == 1:
       lst_n.append(float(y)*2)
    elif float(y)%2 == 0:
       lst_n.append(float(y)/4)
    else:
        print(y)
print('Получившийся список: ',lst_n)
print()

# Способ_3 - самый короткий способ для изменения значений по одному параметру

lst_1 = [4, 8, 7, 9]
print('Изначальный список',lst_1)
change = [item*2 for item in lst_1]
print('Получившийся список: ',change)