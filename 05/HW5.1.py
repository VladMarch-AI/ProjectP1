from keyword import kwlist
from string import punctuation

kwlist = list(kwlist)
lst_w = kwlist[:]
lst_w.append('get')

lst_s = punctuation[:]
lst_s = list(lst_s)
lst_s.remove("_")
lst_s.append(' ')
print(lst_s)

var = input("Enter new name for variable : ")
var_1 = var + "nothing"
print(not var[0].isdecimal() and var_1.islower() and not any(_ in list(var) for _ in lst_s ) and not var in lst_w and not "_" + "_" in var)