a=int(input('Enter value:'))
s=0
temp=a
while(a>0):
        r=a%10
        s=(s*10)+r
        a//=10
if(temp==s):
        print('The value is palindrome')
else:
        print('THe value is not palindrome')

