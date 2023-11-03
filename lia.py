import math

k=7
n=35

prob=0
offspring= 2**k

for i in range(n,offspring+1):
    prob_count = (math.factorial(offspring))/(math.factorial(i)*math.factorial(offspring-i))*((1/4)**i)*((3/4)**(offspring-i))
    prob += prob_count
print(prob)
