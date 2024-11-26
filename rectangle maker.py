#RECTANGLE MAKER

import time
l = int(input("Enter length of Rectangle : "))
b = int(input("Enter width of Rectangle : "))
s = input("Enter character of which Rectangle will be made of : ")

if l>1 and b>1:
    a=""
    for o in range(l-2):
        a+=" "
        
    for x in range(l):
        print(s,end='')
        time.sleep(0.4)

    print('\n',end='')

    for y in range(b-2):
        print(s,a,sep='',end='')
        time.sleep(0.4)
        print(s)
        time.sleep(0.4)

    for z in range(l):
        print(s,end='')
        time.sleep(0.4)

else:
    print("Length and Breadth should be greater than 1")
