# TIC TAC TOE
base="""
         ##          ##         
    1    ##    2     ##    3    
         ##          ##         
################################
         ##          ##         
    4    ##    5     ##    6    
         ##          ##         
################################
         ##          ##         
    7    ##    8     ##    9    
         ##          ##         
"""

x_won=r"""

$$$$\                       $$$$\             $$\      $$\  $$$$$$\  $$\   $$\             $$\ $$\ $$\ 
$$  _|                      \_$$ |            $$ | $\  $$ |$$  __$$\ $$$\  $$ |            $$ |$$ |$$ |
$$ |        $$\   $$\         $$ |            $$ |$$$\ $$ |$$ /  $$ |$$$$\ $$ |            $$ |$$ |$$ |
$$ |        \$$\ $$  |        $$ |            $$ $$ $$\$$ |$$ |  $$ |$$ $$\$$ |            $$ |$$ |$$ |
$$ |         \$$$$  /         $$ |            $$$$  _$$$$ |$$ |  $$ |$$ \$$$$ |            \__|\__|\__|
$$ |         $$  $$<          $$ |            $$$  / \$$$ |$$ |  $$ |$$ |\$$$ |                        
$$$$\       $$  /\$$\       $$$$ |            $$  /   \$$ | $$$$$$  |$$ | \$$ |            $$\ $$\ $$\ 
\____|      \__/  \__|      \____|            \__/     \__| \______/ \__|  \__|            \__|\__|\__|
                                                                                                       
                                                                                                       
                                                                                                       
"""

o_won=r"""

$$$$\                       $$$$\             $$\      $$\  $$$$$$\  $$\   $$\             $$\ $$\ $$\ 
$$  _|                      \_$$ |            $$ | $\  $$ |$$  __$$\ $$$\  $$ |            $$ |$$ |$$ |
$$ |         $$$$$$\          $$ |            $$ |$$$\ $$ |$$ /  $$ |$$$$\ $$ |            $$ |$$ |$$ |
$$ |        $$  __$$\         $$ |            $$ $$ $$\$$ |$$ |  $$ |$$ $$\$$ |            $$ |$$ |$$ |
$$ |        $$ /  $$ |        $$ |            $$$$  _$$$$ |$$ |  $$ |$$ \$$$$ |            \__|\__|\__|
$$ |        $$ |  $$ |        $$ |            $$$  / \$$$ |$$ |  $$ |$$ |\$$$ |                        
$$$$\       \$$$$$$  |      $$$$ |            $$  /   \$$ | $$$$$$  |$$ | \$$ |            $$\ $$\ $$\ 
\____|       \______/       \____|            \__/     \__| \______/ \__|  \__|            \__|\__|\__|
                                                                                                       
                                                                                                       
                                                                                                       
"""
tic_tac_toe=r"""

 ______                ______                     ______                  
/\__  _\__            /\__  _\                   /\__  _\                 
\/_/\ \/\_\    ___    \/_/\ \/    __      ___    \/_/\ \/   ___      __   
   \ \ \/\ \  /'___\     \ \ \  /'__`\   /'___\     \ \ \  / __`\  /'__`\ 
    \ \ \ \ \/\ \__/      \ \ \/\ \L\.\_/\ \__/      \ \ \/\ \L\ \/\  __/ 
     \ \_\ \_\ \____\      \ \_\ \__/.\_\ \____\      \ \_\ \____/\ \____/|
      \/_/\/_/\/____/       \/_/\/__/\/_/\/____/       \/_/\/___/  \/_____/

                                                                          
"""

import time

L1=["1","2","3","4","5","6","7","8","9"]
L2=[38,49,61,170,181,193,302,313,325]

st_win=0
ze_win=0
exit0=0

def win_checker(st_win,ze_win,exit0):
    if base[38]=="*" and base[170]=="*" and base[302]=="*":
        st_win=1
    elif base[49]=="*" and base[181]=="*" and base[313]=="*":
        st_win=1
    elif base[61]=="*" and base[193]=="*" and base[325]=="*":
        st_win=1
    elif base[38]=="*" and base[49]=="*" and base[61]=="*":
        st_win=1
    elif base[170]=="*" and base[181]=="*" and base[193]=="*":
        st_win=1
    elif base[302]=="*" and base[313]=="*" and base[325]=="*":
        st_win=1
    elif base[38]=="*" and base[181]=="*" and base[325]=="*":
        st_win=1
    elif base[61]=="*" and base[181]=="*" and base[302]=="*":
        st_win=1

    elif base[38]=="0" and base[170]=="0" and base[302]=="0":
        ze_win=1
    elif base[49]=="0" and base[181]=="0" and base[313]=="0":
        ze_win=1
    elif base[61]=="0" and base[193]=="0" and base[325]=="0":
        ze_win=1
    elif base[38]=="0" and base[49]=="0" and base[61]=="0":
        ze_win=1
    elif base[170]=="0" and base[181]=="0" and base[193]=="0":
        ze_win=1
    elif base[302]=="0" and base[313]=="0" and base[325]=="0":
        ze_win=1
    elif base[38]=="0" and base[181]=="0" and base[325]=="0":
        ze_win=1
    elif base[61]=="0" and base[181]=="0" and base[302]=="0":
        ze_win=1
    else:
        pass
    
    if st_win==1:
        time.sleep(1)
        print(x_won)
        e(eff="Wanna play again?")
        e(eff="Enter any key to play again or 'e' to exit : ")
        exit0=input()
    elif ze_win==1:
        time.sleep(1)
        print(o_won)
        e(eff="Wanna retry?")
        e(eff="Enter any key to play again or 'e' to exit : ")
        exit0=input()
    else:
        pass
    return exit0

eff='Hello World'
def e(eff):
     for i in eff:
        print(i,end='')
        time.sleep(0.09)
     print('\n')

time.sleep(1)
print(tic_tac_toe)
time.sleep(0.5)
e(eff="Lets Play....!!!")
time.sleep(2)
print(base)
time.sleep(2)

e(eff="The first move will be of '*'....")
e(eff="place where you wanna '*' to be (1 to 9) : ")
int0=input()
if int0 in "123456789":
    base = base.replace(int0,"*")
    time.sleep(0.5)
    print(base)
else:
    time.sleep(0.5)
    print("\nInvalid Input Entered!\n$ Exiting $")
    exit()
    

while exit0!='e':
    for z in range(4):
        print("#       ",z,"        #")
        print("_______________________________________________\n")
        e(eff="'0' turn's now")
        e(eff="place where you wanna '0' to be (1 to 9) : ")
        int0=input()
        if int0 in "123456789":
            base = base.replace(int0,"0")
            time.sleep(0.5)
            print(base)
            win_checker(st_win,ze_win,exit0)
        else:
            time.sleep(0.5)
            print("\nInvalid Input Entered!\n")
            e(eff="Wanna retry?")
            e(eff="Enter any key to play again or 'e' to exit : ")
            exit0=input()
        
        print("_______________________________________________\n")
        e(eff="'*' turn's now")
        e(eff="place where you wanna '*' to be (1 to 9) : ")
        int0=input()
        if int0 in "123456789":
            base = base.replace(int0,"*")
            time.sleep(0.5)
            print(base)
            win_checker(st_win,ze_win,exit0)
        else:
            time.sleep(0.5)
            print("Invalid Input Entered!")
            e(eff="Wanna retry?")
            e(eff="Enter any key to play again or 'e' to exit : ")
            exit0=input()

        if z==3:
            e(eff="Its a Draw!!!, Wanna play again?")
            e(eff="Enter any key to play again or 'e' to exit : ")
            exit0=input()
