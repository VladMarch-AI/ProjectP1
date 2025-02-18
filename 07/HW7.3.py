def second_index(text, some_str):
  first_i = text.find(some_str)
  second_i = text.find(some_str, first_i + 1)
  return second_i if second_i != -1 else None

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')