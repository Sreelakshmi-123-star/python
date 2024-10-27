a=float(input("Enter first side: "))
b=float(input("Enter second side: "))
c=float(input("Enter thirs side: "))

s = (a + b + c) /2

area =(s* (s-a)* (s-b)* (s-c)) **0.5
print("semi permeter is:",s)
print("area of a triangle is:",area)
