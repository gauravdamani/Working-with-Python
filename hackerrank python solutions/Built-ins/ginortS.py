s=input()
l=[]
t=[]
y=[]
n=[]
for i in range(len(s)):
    if s[i].isupper():
        l.append(s[i])
    if s[i].islower():
        t.append(s[i])
    if s[i].isdigit():
        f=int(s[i])
        if f%2==0:
            y.append(f)
        else:
            n.append(f)
t=sorted(t)
l=sorted(l)
n=sorted(n)
y=sorted(y)

for i in range(len(t)):
    print(t[i],end="")
for i in range(len(l)):
    print(l[i],end="")
for i in range(len(n)):
    print(n[i],end="")
for i in range(len(y)):
    print(y[i],end="")