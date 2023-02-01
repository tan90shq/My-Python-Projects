print("Hi, This is a simple calc!")
f = int(input("Tell me first digit!!! : "))
s = int(input("Tell me second digit!!! : "))
op = input("Now tell me yoour operation : ")

op1 = f + s
op2 = f - s
op3 = f * s
op4 = f / s

con = 10

while con > 1:
    if op == "+":
        print(f, "+", s, "=", op1)
    elif op == "-":
        print(f, "-", s, "=", op2)
    elif op == "*":
        print(f, "*", s, "=", op3)
    elif op == "/":
        print(f, "/", s, "=", op4)
    else:
        print("Invalid Input")
        
    f = int(input("Tell me first digit!!! : "))
    s = int(input("Tell me second digit!!! : "))
    op = input("Now tell me yoour operation : ")
    op1 = f + s
    op2 = f - s
    op3 = f * s
    op4 = f / s

