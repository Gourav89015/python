print('enter cordinate (x1,y1) of point A')
x1=int(input('x1='))
y1=int(input('y1='))
print('Point A coordinates are= (%d,%d)'%(x1,y1))
print('enter cordinate (x2,y2) of point B')
x2=int(input('x2='))
y2=int(input('y2='))
print('Point B coordinates are= (%d,%d)'%(x2,y2))
print('enter cordinate (x3,y3) of point C')
x3=int(input('x3='))
y3=int(input('y3='))
print('Point C coordinates are= (%d,%d)'%(x3,y3))
print("                        /\ A(%d,%d)               " %(x1,y1))
print("                       /  \                       ")
print("                      /    \                      ")
print("                     /      \                     ")
print("                    /        \                    ")
print("                   /          \                   ")
print("                  /            \                  ")
print("                 /______________\                 ")
print("             B(%d,%d)           C(%d,%d)          " %(x2,y2,x3,y3))
ar=(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
if ar==0:
    print('Point A,B and C coordinates are in a line')
if ar>0:
        print('Point A,B and C coordinates are not in a line')
if ar<0:
        print('Point A,B and C coordinates are not in a line')
if ar>0:
    z=input('If you want to get area of triangle ABC then enter "1" or not want to get then enter "2"=')   
    if z==1:
        print('Area of triangle ABC is=',ar)
    if z==2:
        print("OK.....................................")
