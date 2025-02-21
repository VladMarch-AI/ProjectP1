def is_palindrome(text):
    from string import punctuation
    my_text = ("".join(item for item in text if item not in punctuation)
               .lower().replace(" ", ""))
    return my_text == my_text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
