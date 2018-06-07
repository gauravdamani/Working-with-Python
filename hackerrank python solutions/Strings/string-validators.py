if __name__ == '__main__':
    s = input()
    c=0
    for i in range(len(s)):
        if s[i].isalnum():
            c=c+1
            print("True")
            break
    if c==0:
        print("False")
    c=0
    for i in range(len(s)):
        if s[i].isalpha():
            c=c+1
            print("True")
            break
    if c==0:
        print("False")
    c=0
    for i in range(len(s)):
        if s[i].isdigit():
            c=c+1
            print("True")
            break
    if c==0:
        print("False")
    c=0
    for i in range(len(s)):
        if s[i].islower():
            c=c+1
            print("True")
            break
    if c==0:
        print("False")
    c=0
    for i in range(len(s)):
        if s[i].isupper():
            c=c+1
            print("True")
            break
    if c==0:
        print("False")