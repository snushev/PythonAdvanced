# Python Cheatsheet

## 🕒 datetime (Работа с дата и час)
```python
import datetime

# Текуща дата и час
now = datetime.datetime.now()

# Създаване на конкретна дата
date = datetime.datetime(2024, 1, 19, 14, 30)

# Форматиране на дата
formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")

# Разбор на низ в дата
parsed_date = datetime.datetime.strptime("2024-01-19", "%Y-%m-%d")
```

---

## 📋 list (Списъци)
```python
# Създаване на списък
nums = [1, 2, 3, 4, 5]

# Добавяне и премахване
nums.append(6)
nums.remove(3)

# Обхождане на списък
for num in nums:
    print(num)

# Подсписък (slicing)
subset = nums[1:4]

# Сортиране и обръщане
nums.sort()
nums.reverse()
```

---

## 📌 tuple (Кортежи)
```python
# Кортежите са неизменяеми списъци
coordinates = (10, 20)

# Извличане на стойности
x, y = coordinates
```

---

## 🎯 set (Множества)
```python
# Създаване на множество
unique_numbers = {1, 2, 3, 4, 4, 2}

# Добавяне и премахване
unique_numbers.add(5)
unique_numbers.remove(2)

# Операции с множества
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2      # {1, 2, 3, 4, 5}
intersection = set1 & set2  # {3}
```

---

## 📖 dict (Речници)
```python
# Създаване на речник
person = {"name": "Alice", "age": 25}

# Достъп до стойности
print(person["name"])

# Добавяне/премахване на ключ
person["city"] = "New York"
del person["age"]
```

---

## 🔤 string (Низове)
```python
text = "Hello, World!"

# Дължина на низ
length = len(text)

# Преобразуване
upper_text = text.upper()
lower_text = text.lower()

# Разделяне и съединяване
words = text.split(", ")
new_text = " - ".join(words)

# Премахване на празни пространства
trimmed = text.strip()

# Проверка за съдържание
contains_hello = "Hello" in text
```

---

## 📂 file (Работа с файлове)
```python
# Четене на файл
with open("file.txt", "r") as file:
    content = file.read()

# Запис във файл
with open("file.txt", "w") as file:
    file.write("Hello, Python!")

# Добавяне към файл
with open("file.txt", "a") as file:
    file.write("\nNew line!")
```

---

## ⚠️ try-except (Обработка на грешки)
```python
try:
    num = int(input("Въведете число: "))
    print(10 / num)
except ValueError:
    print("Грешка: Въведете валидно число.")
except ZeroDivisionError:
    print("Грешка: Деление на нула!")
finally:
    print("Това винаги се изпълнява.")
```
