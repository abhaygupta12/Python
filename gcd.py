def gcd(a,b):
    if a<b:
        small=a
    else:
        small=b
    for i in range(1,small+1):
        if ((a%i==0) and (b%i==0)):
            d=i
    return d
a=int(input("Enter first number="))
b=int(input("Enter second number="))
print(gcd(a,b))
if gcd(a,b)==1:
    print("Retry")
