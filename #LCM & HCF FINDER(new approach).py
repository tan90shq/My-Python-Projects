#LCM & HCF FINDER

num1=int(input("Enter first no. : "))
num2=int(input("Enter second no. : "))
f1=[]
f2=[]
HCF=''
for a in range(1,num1+1):
    if num1%a==0:
        f1+=[a]

for a in range(1,num2+1):
    if num2%a==0:
        f2+=[a]
for i in f1:
    if i in f2:
        HCF=i

print("HCF of no.'s is:-",HCF)
print("LCM of no.'s is:-",num1*num2/HCF)