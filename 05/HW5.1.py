from keyword import kwlist
from string import punctuation

lst_w = list(kwlist)
lst_w.append('get')

lst_s = punctuation
lst_s = list(lst_s.replace('_', ' '))

var = input("Enter new name for variable : ")
var_1 = var + "nothing"
print(not var[0].isdecimal() and var_1.islower() and not any(_ in list(var) for _ in lst_s) and var not in lst_w and not "_" + "_" in var)
