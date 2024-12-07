# ROCK PAPER SCISSORS

import random
import time

rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""
paper="""
    _______
---'   ____)______
          ________)
          _________)
         _________)
---.____________)

"""
scissor="""
    _______
---'   ____)______
          ________)
       ____________)
      (____)
---.__(___)

"""
main=r"""                                                                                                                                           
    .__                  .__                  .__                  .__                  .__                  .__                  .__      
  __|  |___   ______   __|  |___   ______   __|  |___   ______   __|  |___   ______   __|  |___   ______   __|  |___   ______   __|  |___  
 /__    __/  /_____/  /__    __/  /_____/  /__    __/  /_____/  /__    __/  /_____/  /__    __/  /_____/  /__    __/  /_____/  /__    __/  
    |__|                 |__|                 |__|                 |__|                 |__|                 |__|                 |__|                                                                                                                                                
 ._.  __________               __     __________                                _________      .__                                     ._. 
 | |  \______   \ ____   ____ |  | __ \______   \_____  ______   ___________   /   _____/ ____ |__| ______ _________________  ______   | | 
 |_|   |       _//  _ \_/ ___\|  |/ /  |     ___/\__  \ \____ \_/ __ \_  __ \  \_____  \_/ ___\|  |/  ___//  ___/  _ \_  __ \/  ___/   |_| 
 |-|   |    |   (  <_> )  \___|    <   |    |     / __ \|  |_> >  ___/|  | \/  /        \  \___|  |\___ \ \___ (  <_> )  | \/\___ \    |-| 
 | |   |____|_  /\____/ \___  >__|_ \  |____|    (____  /   __/ \___  >__|    /_______  /\___  >__/____  >____  >____/|__|  /____  >   | | 
 |_|          \/            \/     \/                 \/|__|        \/                \/     \/        \/     \/                 \/    |_|                                                                                                                                                                                                                                                                                       
    ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   
   /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/   
"""

time.sleep(1)
print(main)
time.sleep(1)
choices1=['r','p','s']
r,p,s=100,100,100
exit0=''
score_board={"User":0,"Computer":0}
userW,compW=0,0

while exit0!='e':
    print("\nLets Play!")
    print("(Winner decided on the basis of Best of Three games.)\n")
    time.sleep(1)
    for i in range(3):
        user=input("\nChoose:-\n'r' for ROCK.\n'p' for PAPER.\n's'for scissors.\n==>  ").strip().lower()
        pc = random.choices(choices1,weights=[r,p,s],k=1)[0]

        if user not in choices1:
            time.sleep(1)
            print("\nEnter Valid Choice!")
            exit()
        if user==pc:
            if pc=='r':
                time.sleep(0.5)
                print("\nYou Choosed : \n",rock)
                time.sleep(1)
                print("\nComputer Choosed : \n",rock)
                time.sleep(1)
                print("\nIt's a DRAW!")
                r,p,s=r+1,p+1,s+1
            elif pc=='p':
                time.sleep(0.5)
                print("\nYou Choosed : \n",paper)
                time.sleep(1)
                print("\nComputer Choosed : \n",paper)
                time.sleep(1)
                print("\nIt's a DRAW!")
                r,p,s=r+1,p+1,s+1
            else:
                time.sleep(0.5)
                print("\nYou Choosed : \n",scissor)
                time.sleep(1)
                print("\nComputer Choosed : \n",scissor)
                time.sleep(1)
                print("\nIt's a DRAW!")
                r,p,s=r+1,p+1,s+1


        else:
            if user=='r':
                if pc =='p':
                    time.sleep(0.5)
                    print("\nYou Choosed : \n",rock)
                    time.sleep(1)
                    print("\nComputer Choosed : \n",paper)
                    time.sleep(1)
                    print("\nComputer WINS!")
                    p+=1
                    compW+=1
                else:
                    time.sleep(0.5)
                    print("\nYou Choosed : \n",rock)
                    time.sleep(1)
                    print("\nComputer Choosed : \n",scissor)
                    time.sleep(1)
                    print("\nYou WIN!")
                    s-=1
                    userW+=1
            elif user=='p':
                if pc == 'r':
                    time.sleep(0.5)
                    print("\nYou Choosed : \n",paper)
                    time.sleep(1)
                    print("\nComputer Choosed : \n",rock)
                    time.sleep(1)
                    print("\nYou WIN!")
                    r-=1
                    userW+=1
                else:
                    time.sleep(0.5)
                    print("\nYou Choosed : \n",paper)
                    time.sleep(1)
                    print("\nComputer Choosed : \n",scissor)
                    time.sleep(1)
                    print("\nComputer WINS!")
                    s+=1
                    compW+=1
            else:
                if pc=='r':
                    time.sleep(0.5)
                    print("\nYou Choosed : \n",scissor)
                    time.sleep(1)
                    print("\nComputer Choosed : \n",rock)
                    time.sleep(1)
                    print("\nComputer WINS!")
                    r+=1
                    compW+=1
                else:
                    time.sleep(0.5)
                    print("\nYou Choosed : \n",scissor)
                    time.sleep(1)
                    print("\nComputer Choosed : \n",paper)
                    time.sleep(1)
                    print("\nYou WIN!")
                    p-=1
                    userW+=1
    
    if compW>userW:
        score_board["Computer"]+=1
    elif userW>compW:
        score_board["User"]+=1
    else:
        pass
    time.sleep(1.8)
    print("\n\nScore : ",score_board)
    time.sleep(1)
    exit0=input("\nEnter to continue,\nOr press 'e' to exit : ")
    if exit0=='e':
        time.sleep(0.2)
        print("\nexiting...\n")
        time.sleep(1)