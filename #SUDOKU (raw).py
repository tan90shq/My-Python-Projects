#SUDOKU-raw

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



import random
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
    

print(main)
