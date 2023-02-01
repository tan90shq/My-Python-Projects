## GREATEST BETWEEN 3 NUMBER

print("This is the greatest number finder between 3 number")
a = int(input("Enter fist number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if a>b and a>c:
    print("The first number \"",a,"\" is greater than other")
elif b>a and b>c:
    print("The second number \"",b,"\" is greater than other")
elif c>a and c>b:
    print("The third number \"",c,"\" is greater than other")
else:
    print("All number are Equal")
