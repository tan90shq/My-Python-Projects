## THIS IS THE AREA AND CIRCUMFERENCE CALC OF SQUARE,RECTANGLE,TRIANGLE

print("This is the area and circumference calc of square,rectangle,triangle")
inp = input("Please enter the shape (square,rectangle,triangle) : ")

if inp == "square":
    a = int(input("Please give the length of a side : "))
    s1 = a**2
    s2 = a*4
    print("The area of square is",s1)
    print("The perimeter of square is",s2)
    
elif inp == "rectangle":
    b = int(input("Please give the length : "))
    c = int(input("Please give th breath : "))
    r1 = b*c
    r2 = 2*(b+c)
    print("The area of rectangle is",r1)
    print("The perimeter of rectangle is",r2)
    
elif inp=="triangle":
    d = int(input("Please give the height : "))
    e = int(input("Please give the length of base : "))
    t1 = 1/2*(d*e)
    print("The area of triangle is",t1)
    
else:
    print("Invalid input")
    
    
print("\nThank you, Hope you get the answer")