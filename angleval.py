a=float(input('enter 1s1t angle='))
b=float(input('enter 2nd angle='))
c=float(input('enter rd angle='))
sum=float(a+b+c)
if sum==180:
    print('this triangle is valid')
if 180<sum:
    print('triangle with these angles not valid')
if 180>sum:
    print('triangle with these angles not valid')
    
