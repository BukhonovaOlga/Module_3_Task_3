def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(0)
print_params('столбец')
#print_params(3,5,6,7)
print_params(1, "OK")
print_params()

print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ["снег", False, 567]
values_dict = {'a': 'вода', 'b': 342, 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [False, 'жара']
print_params(*values_list_2, 42)