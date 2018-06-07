def average(array):
    l=list(set(array))
    s=0
    for i in l:
        s+=i
    return(s/(len(l)))