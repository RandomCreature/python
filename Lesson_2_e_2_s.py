# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# Способ_1

"""
Как я понял, в данном случае я удаляю из первого списка первое из совпадающих значений.
"""

lst1 = [var1 + var2 for var1 in 'try' if var1 != 'i' for var2 in 'this' if var2 != 'a']
lst2 = [var1 + var2 for var1 in 'or' if var1 != 'i' for var2 in 'that' if var2 != 'a']
print(lst1)
print(lst2)
for i in lst1:
    if i in lst2:
        lst1.remove(i)
        print(lst1)
    else:
        print()

# Способ_2

"""
Преобразую список в множество и спокойно удаляю повторы вычитанием. Проблема: в списке 1 у меня было два повторяющихся значения. При преобразовании осталось, конечно, одно.
"""

lst1 = [var1 + var2 for var1 in 'try' if var1 != 'i' for var2 in 'this' if var2 != 'a']
lst2 = [var1 + var2 for var1 in 'or' if var1 != 'i' for var2 in 'that' if var2 != 'a']
print(lst1)
print(lst2)
set_1 = set(lst1)
set_2 = set(lst2)
lst1=(set_1-set_2)
print(lst1)
