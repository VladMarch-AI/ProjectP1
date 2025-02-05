lst = []
print("List: ", lst)

if len(lst) < 1:
    lst_m = [lst] * 2
    print("List_m: ", lst_m)

elif len(lst) == 1:
    lst_1 = []
    lst_m = [lst] + [lst_1]
    print("List_m: ", lst_m)
else:
    fraction = len(lst) / 2
    fraction = round(fraction + 0.1)
    lst_1 = lst[:fraction]
    lst_2 = lst[fraction:]
    lst_m = [lst_1] + [lst_2]
    print("List_m: ", lst_m)
