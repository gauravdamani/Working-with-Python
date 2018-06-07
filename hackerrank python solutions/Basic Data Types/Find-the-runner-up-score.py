if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    s=set(arr)
    l=list(s)
    l1=sorted(l)
    print(l1[-2])
        