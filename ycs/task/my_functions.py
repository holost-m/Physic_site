from itertools import zip_longest
from re import split as resplit
from re import search


# Преобразует строки с переменными и СИ в Словарь списков [дано, си]
# Приемер{"F": [["36", "км/ч"], ["10", "м/c"]]}
def give_variables_and_si(vars, si):
    res_dct = dict()
    if vars:
        for var, si in zip_longest(vars.split('\n'), si.split('\n'), fillvalue=""):
            value, number = resplit(r'\s?=\s?', var)
            res_dct[value] = [number.split(), si.split()]
    return str(res_dct) # можно считать json-ом


#  Преобразует в корректное решение
def give_correct_solving(solving):
    lst = [search(r'[A-zА-я0-9/=\s+*\-]*', i).group().strip('\r') for i in solving.split('\n')]
    return str(lst)

solving = """F += ma 
a = -F/m
a = 50/25 = -2"""
print(give_correct_solving(solving))



