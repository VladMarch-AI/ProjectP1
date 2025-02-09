lst = []
lst_1 = []
print("list: ", lst)
while 0 in lst:
    lst.remove(0)
    lst_1.append(0)
lst.extend(lst_1)
print("=> List: ", lst)
