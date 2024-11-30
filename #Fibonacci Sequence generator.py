#Fibonacci Sequence generator

n = int(input("Enter no of elements you want in The Fibonacci Sequence : "))
sqn = [0,1]

if n<=0:
    print("Please enter a positive number.")
elif n==1:
    print("The sequence is:- [0]")
else:
    for i in range(n-2):
        sqn+=[sqn[i]+sqn[i+1]]
    print("Your sequence is:-",sqn)
