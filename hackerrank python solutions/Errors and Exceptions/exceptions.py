n=int(input())
for i in range(n):
    arr=input().split()
    try:
         t=int(arr[0])//int(arr[1])
    except ZeroDivisionError as e:
         print ("Error Code:",e)
    except ValueError as e:
         print ("Error Code:",e)
    else:
         print(int(arr[0])//int(arr[1]))
    
         