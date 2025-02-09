lst = []
lst_1 = lst[::2]
print("List: ", lst)
if not lst:
    lst = [0]
print("=>", sum(lst_1), "*", lst[-1], "=>", sum(lst_1) * lst[-1])
