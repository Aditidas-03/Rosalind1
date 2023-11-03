def rabbitsfib(n,k):
    if n==0:
     return 0
    elif n==1:
       return 1
    else:
       return rabbitsfib(n-1,k)+k*rabbitsfib(n-2,k)
    
print (rabbitsfib(33,3))