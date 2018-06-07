if __name__ == '__main__':
    l=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
    l=sorted(l)
    t=[]
    for i in range(len(l)):
        t.append(l[i][1])
    m=set(t)
    f=min(t)
    m.remove(f)
    c=min(m)
    for i in range(len(t)):
        if l[i][1]==c:
            print(l[i][0])

    