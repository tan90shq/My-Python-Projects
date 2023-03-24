import time

t = int(time.strftime("%H"))

name = input("Enter your name : ")
n = name.capitalize()

if t >= 0 and t <= 9:
    print("Good morning,",n,"now wash your face and hit the gym!!!")

elif t >= 9 and t <= 16:
    print("Good afternoon,",n,"and add some protein in your meal you skinny bitch!!!")
    
elif t >= 16 and t <= 19:
    print("Good evening,",n,"and it's time for some walk!!!")
    
elif t >= 19 and t <= 24:
    print("Good night",n,"and it's time for some anime!!!")
    
else:
    print("[Invalid Input], WTF Bro! How's your time wrong.\nAre you aliennn???!!!")