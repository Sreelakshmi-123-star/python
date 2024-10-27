a=int(input("enter a input no: "))
b=int(input("enter a input no: "))
print("\n Select the operation you want:\n1.ADDITION\n2.SUB\n3.MULTIPLY\n4.DIVISION\n5.EXPONENTION5\n6.FLOOR DIVISION\n7.MODULAS \n  ")
m=int(input("Enter the operation you want:"))
if m==1:
    print("ADDITION RESULT IS: ",a+b)
elif m==2:
     print("SUBSTRATION RESSULT IS: ",a-b)
elif m==3:   
     print("MULTIPLY RESULT IS: ",a*b)
elif m==4:   
     print("DIVISION RESULT IS: ",a/b)
elif m==5:   
     print("EXPONENTION RESULT IS: ",a**b)
elif m==6:   
     print("FLOOR DIVISION RESULT IS: ",a//b)
elif m==7:
     print("MODULAS RESULT IS: ",a%b)
else:
     print("invalid")


