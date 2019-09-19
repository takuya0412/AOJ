import math
from decimal import Decimal, ROUND_HALF_UP
while True:
    x=int(input())
    h=int(input())
    if x==h==0:
        break
    bottom_s=x**2
    side_s=math.sqrt(h**2+(x/2)**2)*x*0.5
    s=bottom_s+side_s*4
    print(Decimal(s).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP))
