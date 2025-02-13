hashtag = input("Enter anything: ")

new_hashtag = "".join(_ if _.isalnum() else "" for _ in hashtag.title())
new_hashtag = "#" + new_hashtag
new_hashtag = new_hashtag[:140]
print(new_hashtag)