def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list_ = ['доллар', 5, True]
print_params(*values_list_)

values_dict_ = {'a':1, 'b':True, 'c':'евро' }
print_params(**values_dict_)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)