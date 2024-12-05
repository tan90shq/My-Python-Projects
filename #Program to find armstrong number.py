#Program to check armstrong number

num = input("Enter a number : ")
sum = 0

for i in range(len(num)):
    sum += int(num[i])**int(len(num))
    print('(',num[i],"**",len(num),')',sep='',end='')
    if i != len(num)-1:
        print("+",end='')

print("=",sum)

if sum == int(num):
    print(num,"is a Armstrong number.")
else:
    print(num,"is not a Armstrong number.")