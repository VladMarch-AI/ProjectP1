def common_elements():
  set_1 = {i for i in range(0, 100, 3)}
  set_2 = {i for i in range(0, 100, 5)}
  n_set = set_1.intersection(set_2)
  return n_set


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')
