import random

lst_1 = [random.randint(1, 10) for numbers in range(random.randint(3, 10))]
print("Quantity elements are:", len(lst_1))
print("list: ", lst_1)
lst = [lst_1[0], lst_1[2], lst_1[-2]]
print("New List: ", lst)
