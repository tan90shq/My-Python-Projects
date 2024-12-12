#SUDOKU GAME (Updated)

import random
import time
import math

num=[1,2,3,4,5,6,7,8,9]

layout=r"""
###########################################
#             #             #             #
#   _  _  _   #   _  _  _   #   _  _  _   #
#   _  _  _   #   _  _  _   #   _  _  _   #
#   _  _  _   #   _  _  _   #   _  _  _   #
#             #             #             #
###########################################
#             #             #             #
#   _  _  _   #   _  _  _   #   _  _  _   #
#   _  _  _   #   _  _  _   #   _  _  _   #
#   _  _  _   #   _  _  _   #   _  _  _   #
#             #             #             #
###########################################
#             #             #             #
#   _  _  _   #   _  _  _   #   _  _  _   #
#   _  _  _   #   _  _  _   #   _  _  _   #
#   _  _  _   #   _  _  _   #   _  _  _   #
#             #             #             #
###########################################
"""
layout_temp=r"""
###########################################
#             #             #             #
#   _  _  _   #   _  _  _   #   _  _  _   #
#   _  _  _   #   _  _  _   #   _  _  _   #
#   _  _  _   #   _  _  _   #   _  _  _   #
#             #             #             #
###########################################
#             #             #             #
#   _  _  _   #   _  _  _   #   _  _  _   #
#   _  _  _   #   _  _  _   #   _  _  _   #
#   _  _  _   #   _  _  _   #   _  _  _   #
#             #             #             #
###########################################
#             #             #             #
#   _  _  _   #   _  _  _   #   _  _  _   #
#   _  _  _   #   _  _  _   #   _  _  _   #
#   _  _  _   #   _  _  _   #   _  _  _   #
#             #             #             #
###########################################
"""

list1=[ 93,  96,  99, 107, 110, 113, 121, 124, 127]
list2=[137, 140, 143, 151, 154, 157, 165, 168, 171]
list3=[181, 184, 187, 195, 198, 201, 209, 212, 215]

list4=[357, 360, 363, 371, 374, 377, 385, 388, 391]
list5=[401, 404, 407, 415, 418, 421, 429, 432, 435]
list6=[445, 448, 451, 459, 462, 465, 473, 476, 479]

list7=[621, 624, 627, 635, 638, 641, 649, 652, 655]
list8=[665, 668, 671, 679, 682, 685, 693, 696, 699]
list9=[709, 712, 715, 723, 726, 729, 737, 740, 743]


list01=[93, 137, 181, 357, 401, 445, 621, 665, 709]
list02=[96, 140, 184, 360, 404, 448, 624, 668, 712]
list03=[99, 143, 187, 363, 407, 451, 627, 671, 715]

list04=[107, 151, 195, 371, 415, 459, 635, 679, 723]
list05=[110, 154, 198, 374, 418, 462, 638, 682, 726]
list06=[113, 157, 201, 377, 421, 465, 641, 685, 729]

list07=[121, 165, 209, 385, 429, 473, 649, 693, 737]
list08=[124, 168, 212, 388, 432, 476, 652, 696, 740]
list09=[127, 171, 215, 391, 435, 479, 655, 699, 743]

listMAIN=[list1,list2,list3,list4,list5,list6,list7,list8,list9]
listMAIN_1=[list01,list02,list03,list04,list05,list06,list07,list08,list09]

layout1=0


def sudoku_maker(layout):
    list_temp1=[]
    list_temp2=[]
    list_temp3=[]
    list_temp4=['1','2','3','4','5','6','7','8','9']
    abc=0
    for a in range(9):
        abc=0
        while abc!=1:
            list1=listMAIN[a]
            for b in range(9):
                list01=listMAIN_1[b]
                list_temp1+=list1[:b]
                list_temp2+=list01[:a]
                list_temp3=list_temp1+['abc']+list_temp2
                    
                for c in list_temp3:
                    try:
                        list_temp4.remove(layout[c])
                    except:
                        continue
                if list_temp4!=[]:
                    layout=list(layout)
                    layout[list1[b]]=random.choice(list_temp4)
                    list_temp1.clear()
                    list_temp2.clear()
                    list_temp3.clear()
                    layout=''.join(layout)
                    list_temp4=['1','2','3','4','5','6','7','8','9']
                    
                    if b==8:
                        abc+=1          
                else:
                    list_temp1.clear()
                    list_temp2.clear()
                    list_temp3.clear()
                    list_temp4=['1','2','3','4','5','6','7','8','9']
                    break
    return layout


def soduku_randomizer(layout,layout1,empty_spc):
    layout1=list(layout)
    for i in range(9):
        list1=listMAIN[i].copy()
        list1=random.choices(list1,k=empty_spc)
        for x in list1:
                layout1[x]='_'
    layout1=''.join(layout1)
    return layout1


sudoku=r"""

 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || | _____  _____ | || |  ________    | || |     ____     | || |  ___  ____   | || | _____  _____ | |
| |   /  ___  |  | || ||_   _||_   _|| || | |_   ___ `.  | || |   .'    `.   | || | |_  ||_  _|  | || ||_   _||_   _|| |
| |  |  (__ \_|  | || |  | |    | |  | || |   | |   `. \ | || |  /  .--.  \  | || |   | |_/ /    | || |  | |    | |  | |
| |   '.___`-.   | || |  | '    ' |  | || |   | |    | | | || |  | |    | |  | || |   |  __'.    | || |  | '    ' |  | |
| |  |`\____) |  | || |   \ `--' /   | || |  _| |___.' / | || |  \  `--'  /  | || |  _| |  \ \_  | || |   \ `--' /   | |
| |  |_______.'  | || |    `.__.'    | || | |________.'  | || |   `.____.'   | || | |____||____| | || |    `.__.'    | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
"""

print(sudoku)

consent=input("wanna solve Sudoku? (y/n) : ").strip().lower()
if consent!='y':
    print("\nSee you later!")
    print("Exiting...\n")
    exit()


while True:
    time.sleep(1)
    diff=input("\nEnter the difficulty (easy/mid/hard) : ").strip().lower()
    if diff not in ['easy', "mid", "hard"]:
        print("\nPlease choose valid difficulty.\n")
        exit()
    time.sleep(1)
    print("\nPlease Wait... ")
    list1=listMAIN[0]
    layout=sudoku_maker(layout)

    if diff=='easy':
        layout1=soduku_randomizer(layout,layout1,3)
    elif diff=='mid':
        layout1=soduku_randomizer(layout,layout1,5)
    else:
        layout1=soduku_randomizer(layout,layout1,7)

    print("\nINSTRUCTIONS:-")
    input("Press enter to see puzzle, the timer will begin after you hit enter,\nPress enter again to see SOLUTION and stop the timer.\nGOOD LUCK! : ")
    st_time=time.time()
    print("\nHere is your Puzzle : ",layout1,sep='\n\n\n')
    input('\n==> ')
    end_time=time.time()

    print("\nHere is the Solution : ",layout,sep='\n\n\n')
    print("\nTime taken : ",math.ceil(end_time-st_time),'sec')
    exit0=input("\nEnter to play again or enter 'e' to exit : ")
    if exit0=='e':
        print("\nSee you later!")
        print("Exiting...\n")
        exit()
    print("\nLets play again!")
    layout=layout_temp