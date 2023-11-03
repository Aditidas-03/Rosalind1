

def rabbitsfib(n,m):
    rabbits = [1,1]
    for age in range (2,n):
        if age<m:
            rabbits.append(rabbits[-2]+rabbits[-1])
        elif age == m :
            rabbits.append(rabbits[-2]+rabbits[-1]-1)
        else:
            rabbits.append(rabbits[-2]+rabbits[-1]-rabbits[-(m+1)])
        
    return rabbits[-1]
print(rabbitsfib(89,18))