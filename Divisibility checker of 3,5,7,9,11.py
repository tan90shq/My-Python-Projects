## DIVISIBILITY CHECKER OF 3,5,7,9,11

print("This is the divisibility checker of 3,5,7,9,11")

a = int(input("Enter a number : "))

b = a%3
c= a%5
d = a%11
e = a%7
f = a%9

if b==0:
    print("The number is divisible by 3")
    
elif c==0:
    print("The number is divisible by 5")
    
elif e==0:
    print("The number is divisible by 7")
    
elif f==0:
    print("The number is divisible by 9")
    
elif d==0:
    print("The number is divisible by 11")
    
else:
    print("The number is not divisible by 3,5,11")