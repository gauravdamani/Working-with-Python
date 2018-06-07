cube = lambda x:x*x*x # complete the lambda function 

def fibonacci(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        lst = fibonacci(n-1)
        lst.append(lst[-1] + lst[-2])
        return lst# return a list of fibonacci numbers