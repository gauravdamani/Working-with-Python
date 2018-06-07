def print_formatted(number):
    l=len(bin(number)[2:])
    for i in range(1,number+1):
        s="{0:{l}d} {0:{l}o} {0:{l}X} {0:{l}b}".format(i,l=l)
        print(s)