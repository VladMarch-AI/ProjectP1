def add_one(some_list):
  number = int(str(some_list)[1:-1].replace(",", "").replace(" ", "")) + 1
  my_list = []
  for element in str(number):
      my_list.append(int(element))
  return my_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
