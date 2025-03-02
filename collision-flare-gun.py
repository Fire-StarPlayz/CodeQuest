import decimal
def round_to_nearest_decimal(number):
    context = decimal.getcontext()
    context.rounding = decimal.ROUND_HALF_UP
    if number*10 is int:
        return str(number)
    else:
        return decimal.Decimal(str(number)).quantize(decimal.Decimal('.01'))

for i in range(int(input())):
    v1, m1, v2, m2 = (input().split(','))
    L1 = float(m1)*float(v1)
    L2 = float(m2)*float(v2)
    print(round_to_nearest_decimal((L1+L2)/(float(m1)+float(m2))))
