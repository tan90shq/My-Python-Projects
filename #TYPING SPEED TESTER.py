#TYPING SPEED TESTER

import random
import time

sent_easy = [
    'The sky turns orange during sunset.',
    'Books take us to different worlds.',
    'Children love playing in the rain.',
    'A smile can brighten someone’s day.',
    'Music makes people feel happy or relaxed.',
    'Flowers bloom beautifully in the spring.',
    'Laughter often spreads quickly in a group.',
    'A cat purring softly feels comforting.',
    'Clouds sometimes look like shapes or animals.',
    'Drawing with crayons can be fun for everyone.'
]

sent_med = [
    'Some people find joy in painting even if they are not artists.',
    'A quiet forest can feel peaceful yet mysterious at the same time.',
    'Watching a bird build its nest can be surprisingly calming.',
    'The smell of freshly baked bread often reminds people of home.',
    'Taking a walk under the stars can inspire deep thoughts.',
    'The crackling of a fireplace makes winter evenings cozy.',
    'Writing letters to friends can feel more personal than sending texts.',
    'An old photo album can bring back memories long forgotten.',
    'A gentle breeze on a hot day feels like nature’s gift.',
    'Trying something new often brings unexpected happiness.'
]

sent_hard = [
    'Writing a poem often involves balancing emotions with rhythm.',
    'A single decision can ripple through time, changing a person’s life forever.',
    'The contrast between urban chaos and rural calm is fascinating to observe.',
    'Philosophy challenges people to question the nature of reality itself.',
    'The complexities of human emotions are often reflected in art and literature.',
    'The delicate balance between freedom and responsibility shapes our choices.',
    'The vastness of the ocean can make one feel both awestruck and insignificant.',
    'Understanding another person’s perspective requires empathy and patience.',
    'Time often feels slow in moments of pain but flies in moments of joy.',
    'Creativity thrives in spaces where curiosity and courage meet.'
]

time.sleep(1)
art=r"""
          ______          _                ____                __    ______        __         
         /_  __/_ _____  (_)__  ___ _     / __/__  ___ ___ ___/ /   /_  __/__ ___ / /____ ____
          / / / // / _ \/ / _ \/ _ `/    _\ \/ _ \/ -_) -_) _  /     / / / -_|_-</ __/ -_) __/
         /_/  \_, / .__/_/_//_/\_, /    /___/ .__/\__/\__/\_,_/     /_/  \__/___/\__/\__/_/   
        _____/___/_/__________/___/________/_/______________________________________________  
       /___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/  
"""

print(art)
time.sleep(1)
diff=input("\n\nChoose difficulty (easy/mid/hard) : ").strip().lower()
queL=[]
total_char=0
total_miss=0
total_skip=0
all_char=[]
dict_of_missed_words={}

if diff=='easy':
    queL.extend(random.choices(sent_easy,k=3)+random.choices(sent_med,k=2))
elif diff=='mid':
    queL.extend(random.choices(sent_easy,k=1)+random.choices(sent_med,k=3)+random.choices(sent_hard,k=1))
elif diff=='hard':
    queL.extend(random.choices(sent_med,k=2)+random.choices(sent_hard,k=3))
else:
    print("Enter Valid Difficulty!!!")
    exit()
time.sleep(0.5)
input("\nPress Enter to start Test : ")
time_strt=time.time()                                                                  
sent_int = []

time.sleep(0.15)
for i in queL:
    print("\n______________________________________________________________________________________________________________________________________________________________________\n")
    print(i,'\n')
    sent_int+=[input("Type here : \n")]

time_stop=time.time()                                                                 
time_taken=time_stop-time_strt

for i in range(len(queL)):
    total_char+=len(queL[i].split())
    all_char+=queL[i].split()
    for x in range(len(queL[i].split())):
        try:
            if queL[i].split()[x]==sent_int[i].split()[x]:
                pass
            else:
                total_miss+=1
                if queL[i].split()[x] not in dict_of_missed_words:
                    dict_of_missed_words[queL[i].split()[x]]=sent_int[i].split()[x]
                else:
                    for z in range(1,all_char.count(queL[i].split()[x])):
                        renamed =queL[i].split()[x] + '_' + str(z+1)
                        dict_of_missed_words[renamed]=sent_int[i].split()[x]

        except:
            total_skip+=1

time.sleep(0.5)
print("\nGenerating result...")
time.sleep(2)
print("\nResult :-\n")
time.sleep(0.5)
print("Total words : ",total_char)
print("Words Misstyped : ",total_miss,sep='')
print("Words Skipped : ",total_skip,sep='')
print("Accuracy : ", 100-(((total_miss+total_skip)*100)//total_char),' %',sep='')
print("Words Per Minute(WPM) [avg:-40 wpm] : ",((total_char-(total_miss+total_skip))*60)//time_taken," WPM",sep='')
time.sleep(1.5)
view_dict=input("\nWanna see misstyped words? (y/n) : ").strip().lower()

if view_dict=='y':
    time.sleep(0.4)
    print("\nHere is the Dictionary of misstyped words {Correct word : Typed word} : \n\n\n",dict_of_missed_words,"\n\n\nCome again for Retest!\n",sep='')

else:
    time.sleep(0.4)
    print("\nCome again for Retest!\n")
    exit()
