s = input()
if len(s) > 0:
    li = list(s)[::-1]
    if ''.join(li) != s:
        return False
return True
