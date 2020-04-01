"""Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""
initial_list = []
i = int(input('введите количество элементов будущего списка: '))
for item in range(i):
    item = input(f'введите {item} элемент списка: ')
    initial_list.append(item)
print(initial_list)
new_list = []
index: int

try:
    for index in range(i)[::2]:
        new_list.append(initial_list[index+1])
        new_list.append(initial_list[index])
except Exception: None
if i % 2 != 0:
    new_list.append(initial_list[i-1])
print(new_list)