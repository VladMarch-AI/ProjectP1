ans = (input("Enter number: "))
while len(ans) > 1:
    while len(ans) > 1:
        ans = list(ans)
        _ = int(ans[0]) * int(ans.pop())
        ans[0] = _
    ans = int(ans[0])
    ans = str(ans)
    ans = list(ans)
    if int(ans[0]) > 9:
        continue
ans = int(ans[0])
print(ans)
