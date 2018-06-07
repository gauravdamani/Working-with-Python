n=int(input())
for i in range(n):
    s=input()
    if (s[0]=='8' or s[0]=='9' or s[0]=='7') and len(s)==10 and s.isdigit():
        print("YES")
    else:
        print("NO")