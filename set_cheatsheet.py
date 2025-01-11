# === SET CHEATSHEET ===

# Създаване на множество
my_set = {1, 2, 3}               # С множество от елементи
empty_set = set()                # Празно множество (НЕ {})
my_set_from_list = set([1, 2, 2, 3])  # Преобразува списък -> {1, 2, 3}

# Добавяне и премахване на елементи
my_set.add(4)                    # Добавя елемент -> {1, 2, 3, 4}
my_set.remove(3)                 # Премахва елемент (KeyError, ако го няма)
my_set.discard(5)                # Премахва елемент (без грешка, ако го няма)
my_set.pop()                     # Премахва и връща случаен елемент
my_set.clear()                   # Изчиства множеството -> set()

# Проверки
3 in my_set                      # Проверява дали елемент е в множеството
3 not in my_set                  # Проверява дали елемент НЕ е в множеството
len(my_set)                      # Размер на множеството

# Операции между множества
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Обединение (Union)
union_set = set1 | set2          # {1, 2, 3, 4, 5}
union_set = set1.union(set2)     # Същото

# Сечение (Intersection)
intersection_set = set1 & set2   # {3}
intersection_set = set1.intersection(set2)

# Разлика (Difference)
difference_set = set1 - set2     # {1, 2}
difference_set = set1.difference(set2)

# Симетрична разлика (Symmetric Difference)
symmetric_diff = set1 ^ set2     # {1, 2, 4, 5}
symmetric_diff = set1.symmetric_difference(set2)

# Подмножество и надмножество
set1 <= set2                     # True, ако set1 е подмножество на set2
set1.issubset(set2)              # Същото
set1 >= set2                     # True, ако set1 е надмножество на set2
set1.issuperset(set2)            # Същото

# Проверка за дискретност (нямат общи елементи)
set1.isdisjoint(set2)            # True, ако нямат общи елементи
