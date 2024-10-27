a=10
b=5
a=5
b=10
print("value of a before swapping",a)
print("value of a before swapping",b)
temp=a
a=b
b=temp
print("value of a after swapping",a)
print("value of a after swapping",b)
print("\n WITHOUT USING ANOTHER VARIABLE")
a=10
b=5
print("value of a before swapping",a)
print("value of a before swapping",b)
a=a+b
b=a-b
a=a-b
print("value of a after swapping",a)
print("value of a after swapping",b)