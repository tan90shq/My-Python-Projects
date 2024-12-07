#TYPING SPEED TESTER

import random
import time

sent_easy = [
    'The sky turns orange during sunset.',
    'Books take us to different worlds.',
    'Children love playing in the rain.',
    'A smile can brighten someone’s day.',
    'Music makes people feel happy or relaxed.'
]

sent_med = [
    'Some people find joy in painting even if they are not artists.',
    'A quiet forest can feel peaceful yet mysterious at the same time.',
    'Watching a bird build its nest can be surprisingly calming.',
    'The smell of freshly baked bread often reminds people of home.',
    'Taking a walk under the stars can inspire deep thoughts.'
]

sent_hard = [
    'Writing a poem often involves balancing emotions with rhythm.',
    'A single decision can ripple through time, changing a person’s life forever.',
    'The contrast between urban chaos and rural calm is fascinating to observe.',
    'Philosophy challenges people to question the nature of reality itself.',
    'The complexities of human emotions are often reflected in art and literature.'
]



diff=input("Choose difficulty (easy/mid/hard) : ").strip().lower()
queL=[]
total_char=0
total_miss=0

if diff=='easy':
    queL.extend(random.choices(sent_easy,k=3)+random.choices(sent_med,k=2))
elif diff=='mid':
    queL.extend(random.choices(sent_easy,k=1)+random.choices(sent_med,k=3)+random.choices(sent_hard,k=1))
elif diff=='hard':
    queL.extend(random.choices(sent_med,k=2)+random.choices(sent_hard,k=3))
else:
    print("Enter Valid Difficulty!!!")
    exit()

input("\nPress Enter to start Test : ")
time_strt=time.time()                                                                 
sent_int = []

for i in queL:
    print("\n______________________________________________________________________________________________________________________________________________________________________\n")
    print(i,'\n')
    sent_int+=[input("Type here : \n")]

time_stop=time.time()                                                                   
time_taken=time_stop-time_strt

for i in range(len(queL)):
    total_char+=len(queL[i].split())
    for x in range(len(queL[i].split())):
        try:
            if queL[i].split()[x]==sent_int[i].split()[x]:
                pass
            else:
                total_miss+=1
        except:
            continue
print("\nResult :-\n")
print("Total words : ",total_char)
print("Words Misstyped : ",total_miss,sep='')
print("Accuracy : ", 100-((total_miss*100)//total_char),' %',sep='')
print("Words Per Minute(WPM) [avg:-40 wpm] : ",((total_char-total_miss)*60)//time_taken," WPM",sep='')
