a=int(input("enter no.=-"))
s=0

while a>=1:
    b=int(a%10)
    c=int(a-b)
    s=int(s+b)
    a=int(c/10)
    if a==0:
        print(s)
    

