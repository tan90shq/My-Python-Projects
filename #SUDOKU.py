#SUDOKU-006
import random
import time
def row_check(row,colm):
    for i in range(colm):
        if main[row][i] in num:
            num.remove(main[row][i])


def colm_check(row,colm):
    for i in range(row):
        if main[i][colm] in num:
            num.remove(main[i][colm])


def grid_check(row,colm):
    if row%3!=0:
        if row in [1,2]:
            check_point1=0
        elif row in [4,5]:
            check_point1=3
        else:
            check_point1=6

        if colm in [0,1,2]:
            check_point2=0
        elif colm in [3,4,5]:
            check_point2=3
        else:
            check_point2=6

        for x in range(check_point1,check_point1+3):
            for y in range(check_point2,check_point2+3):
                if x==row and y==colm:
                    break
                else:
                    if main[x][y] in num:
                        num.remove(main[x][y])
            if x==row and y==colm:
                break

def unsolved_sudoku_builder(layout,blanks):
    layout=list(layout)
    for x in range(9):
        ch=random.choices(positions[x],k=random.choice(blanks))
        for y in ch:
            layout[y]='_'
    layout=''.join(layout)
    return layout


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




while True:
    main=[
    [0,0,0,   0,0,0,  0,0,0],
    [0,0,0,   0,0,0,  0,0,0],
    [0,0,0,   0,0,0,  0,0,0],

    [0,0,0,   0,0,0,  0,0,0],
    [0,0,0,   0,0,0,  0,0,0],
    [0,0,0,   0,0,0,  0,0,0],

    [0,0,0,   0,0,0,  0,0,0],
    [0,0,0,   0,0,0,  0,0,0],
    [0,0,0,   0,0,0,  0,0,0]
    ]

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
    positions=[
    [ 93,  96,  99, 107, 110, 113, 121, 124, 127],
    [137, 140, 143, 151, 154, 157, 165, 168, 171],
    [181, 184, 187, 195, 198, 201, 209, 212, 215],
    [357, 360, 363, 371, 374, 377, 385, 388, 391],
    [401, 404, 407, 415, 418, 421, 429, 432, 435],
    [445, 448, 451, 459, 462, 465, 473, 476, 479],
    [621, 624, 627, 635, 638, 641, 649, 652, 655],
    [665, 668, 671, 679, 682, 685, 693, 696, 699],
    [709, 712, 715, 723, 726, 729, 737, 740, 743]
    ]

    print("\n\n\n________________________________________________________________________________________________________________________\n")
    print(sudoku)
    print("\n________________________________________________________________________________________________________________________")
    consent=input("\n===>>> wanna solve Sudoku? (yes/no) : ").strip().lower()
    if consent!='yes':
        print("\nSee you later!")
        print("Exiting...\n")
        break

    diff=input("\n===>>> Enter the difficulty (easy/mid/hard) : ").strip().lower()
    if diff not in ['easy', "mid", "hard"]:
        print("\n@!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!@\nPlease choose valid difficulty.\n@!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!@")
        continue

    #####-----BUIDER-----#####
    row,colm=0,0
    num=[1,2,3,4,5,6,7,8,9]

    while row<9 and colm<9:
        try:
            num=[1,2,3,4,5,6,7,8,9]
            row_check(row,colm)
            colm_check(row,colm)
            grid_check(row,colm)
            main[row][colm]=random.choice(num)

        except IndexError:
            row-=1
            colm=0

        colm+=1
        if colm==9:
            colm=0
            row+=1
    #####----------------#####

    #####-----list to ASCII-----#####
    layout=list(layout)
    for x in range(9):
        for y in range(9):
            layout[positions[x][y]]=str(main[x][y])
    layout=''.join(layout)
    #####-----------------------#####


    if diff=='easy':
        unsolved_layout=unsolved_sudoku_builder(layout,[1,2,3])
    elif diff=='mid':
        unsolved_layout=unsolved_sudoku_builder(layout, [3,4,5])
    else:
        unsolved_layout=unsolved_sudoku_builder(layout,[3,4,5,6])

    input("""
          

          +------------+
          |INSTRUCTIONS|
          +------------+
-> To input any number you have to type it in this format:-
          "<number> [<row>,<column>]"
          
-> Eg:- for inserting 7 in row 2 & column 5;
          Input--> '7 [2,5]'

-> The Timer will start after you hit enter

          
          
===>>> Press [ENTER] to Start : """)
    start_time=time.time()
    while unsolved_layout!=layout:

        print("________________________________________________________________________________________________________________________")
        print("                                                                            Time Taken Till Now : ", int(time.time()-start_time),'seconds...')
        print(unsolved_layout,'\n')

        #####-----Answer Error Handling-----#####
        while True:
            answer=input("===>>> Enter your answer : ").strip().split()
            try:
                answer[0],answer[1]=eval(answer[0]),eval(answer[1])
                answer[1][0],answer[1][1]=answer[1][0]-1,answer[1][1]-1
                if answer[0] not in [1,2,3,4,5,6,7,8,9] or answer[1][0] not in [0,1,2,3,4,5,6,7,8] or answer[1][1] not in [0,1,2,3,4,5,6,7,8]:
                    print("\n@!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!@\nPlease Enter correct Values!\nThe values must be 'From 1 to 9'\n@!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!@\n")
                else:
                    break
            except:
                print("\n@!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!@\nPlease Enter correct format!\nEg:- for inserting 7 in row 2 & column 5;\n     Input--> '7 [2,5]'\n@!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!@\n")
        #####-------------------------------#####

        if unsolved_layout[positions[answer[1][0]][answer[1][1]]]=='_':
            if answer[0]==main[answer[1][0]][answer[1][1]]:
                unsolved_layout=list(unsolved_layout)
                unsolved_layout[positions[answer[1][0]][answer[1][1]]]=str(answer[0])
                unsolved_layout=''.join(unsolved_layout)
                print("\n    ~{ You are correct! }  ~    \n")
            else:
                print("\n    ~{ you are wrong! }~    \n")
        else:
            print("\n    ~{ The space is already filled! }~    \n")
    
    print("\n\n________________________________________________________________________________________________________________________")
    print("\n      +---------------------+\n----> ! ~CONGRATS, YOU WON~ ! <----\n      +---------------------+\n")
    print("~$$$ Total Time Taken : ", int(time.time()-start_time),'seconds...    OR    ', int(time.time()-start_time)//60, 'minutes...')
    print("\n________________________________________________________________________________________________________________________")
    input("\n\n===>>> [ENTER] to play again : ")