#RANDOM PASSWORD GENERATOR

import random

alphaC='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphaS='abcdefghijklmnopqrstuvwxyz'
num='1234567890'
smybl='@#$._'

length=int(input("Enter length of password (b/w 4 to 17) : "))
if length<4 or length>17:
    print("\nEnter valid password length")
    exit()

is_num=input("Wanna include numbers? (y/n) : ")
is_smybl=input("Wanna include symbols? (y/n) : ")
freq=[0,0,0,0]
freq_element=4
pass0 = ''
passL = ''


def freq_decider(length,freq,freq_element,num):
    if is_num=='y' and is_smybl!='y':
        freq_element=3
    elif is_num!='y' and is_smybl=='y':
        freq_element=3
    elif is_num!='y' and is_smybl!='y':
        freq_element=2
    else:
        pass

    while length!=sum(freq):
        freq = random.choices(num[:9],k=freq_element)
        for i in freq:
            freq[freq.index(i)] = int(i)
    return freq
#freq=freq_decider(length,freq,freq_element,num)                #  [ save freq like this ]
freq=freq_decider(length,freq,freq_element,num)


def pass_gen(pass0,passL):
    try:
        for i in range(freq[0]):
            pass0 += random.choice(alphaC)
        for i in range(freq[1]):
            pass0 += random.choice(alphaS)
        for i in range(freq[2]):
            pass0 += random.choice(num)
        for i in range(freq[3]):
            pass0 += random.choice(smybl)
    
    except:
        pass
    passL=list(pass0)
    pass0=''
    random.shuffle(passL)
    for i in passL:
        pass0+=i
    return pass0

# pass0=pass_gen(pass0,passL)                #  [ save pass0 like this ]


def main(freq,pass0):
    if is_num=='y' and is_smybl=='y':
        pass0 = pass_gen(pass0,passL)
        print("Your password is : ",pass0)
    elif is_num=='y' and is_smybl!='y':
        freq.insert(3,0)
        pass0 = pass_gen(pass0,passL)
        print("Your password is : ",pass0)
    elif is_num!='y' and is_smybl=='y':
        freq.insert(2,0)
        pass0 = pass_gen(pass0,passL)
        print("\nYour password is : ",pass0)
    elif is_num!='y' and is_smybl!='y':
        pass0 = pass_gen(pass0,passL)
        print("\nYour password is : ",pass0)
    else:
        print('Error Occured!!!\nExiting....')
        exit()

main(freq,pass0)
