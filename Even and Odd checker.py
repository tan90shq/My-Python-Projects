## EVEN OR ODD CHECKER

print("This is even or odd checker")

inp = int(input("Enter a number : "))
result = inp%2

if inp == 0:
    print("The number is zero")

elif result==0:
    print("The number is even")
    
else:
    print("The number is odd")