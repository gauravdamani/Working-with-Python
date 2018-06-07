import re
n=int(input())
for i in range(n):
    s=input()
    try:
        re.compile(s)
    except re.error:
        print(False)
    else:
        print(True)