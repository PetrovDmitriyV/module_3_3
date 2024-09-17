def print_params(a=1, b='строка', c=True):
    print(a, b, c)


#   1.Функция с параметрами по умолчанию:

print_params()
print_params(a=4, b=5, c='ok')
print_params(a=4, b=5)
print_params(b=25)
print_params(c=[1, 2, 3])

#   2.Распаковка параметров:

values_list = (1, 'No', [6, 5])
values_dict = {'a': 4, 'b': 'Ok', 'c': False}
print_params(*values_list)
print_params(**values_dict)
print_params(a=values_list, b=values_dict)

#   3.Распаковка + отдельные параметры:

values_list_2 = ('Hello', 32)
print_params(*values_list_2, 42)


def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
        list_my.append(item)
    print(item)
    print(list_my)


append_to_list(10)
append_to_list('15')
append_to_list(20, 30)

