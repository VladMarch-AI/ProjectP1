def correct_sentence(text):
  text = list(text)
  if text[-1] != ".":
    text.append(".")
  n_text = text[0].title()
  text[0] = n_text
  text = ''.join(text)
  return f"{text}"

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
