def popular_words(text, words):
  numb = []
  for word in words:
      numb.append(text.lower().split().count(word))
  return dict(zip(words, numb))


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
