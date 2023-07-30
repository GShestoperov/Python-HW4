# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите n: "))
m = int(input("Введите m: "))

list_n = []
list_m = []
for i in range(n):
    list_n.append(int(input(f"Введите {i+1}-ое число множества n: ")))
for i in range(m):
    list_m.append(int(input(f"Введите {i+1}-ое число множества m: ")))

print(list_n)
print(list_m)

list_res = []
for item in list_n:
    if item in list_m:
        list_res.append(item)
for item in list_m:
    if item in list_n:
        list_res.append(item)

list_res = list(set(list_res))  # удаляем повторы
list_res.sort()  # сортируем по возрастанию

print(f"Результат: {list_res}")
