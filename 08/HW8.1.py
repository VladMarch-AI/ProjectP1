def add_one(some_list):
  some_list = int(str(some_list)[1:-1].replace(",", "").replace(" ", ""))
  some_list += 1
  some_list = str(some_list)
  my_list = []
  for element in some_list:
      element = int(element)
      my_list.append(element)
  return my_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
