from inspect import isgenerator


def prime_generator(end):
  def simple_n(n):
    if n < 2:
        return False
    for el in range(2, int(n ** 0.5) + 1):
        if n % el == 0:
            return False
    return True

  for el_ in range(2, end + 1):
      if simple_n(el_):
          yield el_


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
