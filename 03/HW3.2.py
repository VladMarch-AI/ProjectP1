lst = []
print("List_1: ", lst)
if len(lst) >= 2:
    element = lst.pop()
    lst.insert(0, element)
    print("List_2: ", lst)
else:
    print("List_2: ", lst)
