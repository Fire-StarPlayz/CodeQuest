import math
for i in range(int(input())):
    cf = input()
    cost = float(cf.strip('$'))*100
    q = str(math.floor(cost/25))
    cost = cost%25 
    d = str(math.floor(cost/10))
    cost = cost%10
    n = str(math.floor(cost/5))
    cost = cost%5
    p = str(math.floor(cost/1))
    print(cf)
    print("Quarters="+q)
    print("Dimes="+d)
    print("Nickels="+n)
    print("Pennies="+p)