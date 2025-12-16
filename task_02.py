s = input()
if len(s) > 0:
    li = list(s)[::-1]
    print(''.join(li) == s)
else:
    print(True)
