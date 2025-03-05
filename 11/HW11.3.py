def is_even(number):
  str_n = str(number)
  if str_n[-1] in ['1', '3', '5', '7', '9']:
      return False
  else:
      return True


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('OK')
