#TYPING SPEED TESTER

import random
import time

sent_easy = [
    'The Earth revolves around the Sun.',
    'Plants need sunlight to grow.',
    'Dogs are loyal animals and make great pets.',
    'Water freezes at 0 degrees Celsius.',
    'Smartphones help people connect with others.',
    'Birds build nests to lay their eggs.',                                                      # by AI
    'Rainbows appear after it rains when sunlight hits water droplets.',                        
    'Chocolate is made from cocoa beans.',
    'The moon looks bright because it reflects sunlight.',
    'Bees collect nectar to make honey.'
]

sent_med = [
    'A healthy diet includes fruits, vegetables, and proteins.',
    'The Pythagorean theorem helps calculate the sides of right-angled triangles.',
    'Solar panels convert sunlight into electricity using photovoltaic cells.',
    'Gravity is the force that keeps planets in orbit around the Sun.',
    'The human brain controls thoughts, emotions, and actions.',                                            # by AI
    'The invention of the printing press revolutionized communication in the 15th century.',
    'Vaccines work by training the immune system to fight specific diseases.',
    'Sustainable development focuses on meeting present needs without harming future generations.',
    'Electric cars reduce pollution compared to gasoline-powered vehicles.',
    'Photosynthesis is the process by which plants convert carbon dioxide into oxygen and glucose.'
]

sent_hard = [
    'Black holes have gravitational forces so strong that nothing, not even light, can escape.',
    'Quantum computing uses qubits, which can represent both 0 and 1 simultaneously, unlike classical bits.',
    'Genetic engineering enables scientists to modify DNA to treat diseases or enhance crops.',
    'Plate tectonics explains the movement of Earth\'s crustal plates, leading to earthquakes and volcanic eruptions.',
    'The Higgs boson particle provides mass to other particles through interactions in the Higgs field.',                      # by AI
    'Cryptography ensures secure communication by encrypting data into unreadable formats without a decryption key.',
    'The study of dark matter aims to understand the missing mass in the universe that does not emit detectable radiation.',
    'Neural networks, a type of AI, mimic the structure of the human brain to process complex data patterns.',
    'Renewable energy sources like wind and solar power require efficient storage solutions to ensure reliability.',
    'Cultural relativism in anthropology suggests that no culture is superior to another and should be understood on its own terms.'
]


diff=input("Choose difficulty (easy/mid/hard) : ").strip().lower()
queL=[]
total_char=0
total_miss=0

if diff=='easy':
    queL.extend(random.choices(sent_easy,k=1)+random.choices(sent_med,k=0))
elif diff=='mid':
    queL.extend(random.choices(sent_easy,k=1)+random.choices(sent_med,k=3)+random.choices(sent_hard,k=1))
elif diff=='hard':
    queL.extend(random.choices(sent_med,k=2)+random.choices(sent_hard,k=3))
else:
    print("Enter Valid Difficulty!!!")
    exit()

input("\nPress Enter to start Test : ")
time_strt=time.time()                                                                  # by AI
sent_int = []

for i in queL:
    print("\n______________________________________________________________________________________________________________________________________________________________________\n")
    print(i,'\n')
    sent_int+=[input("Type here : \n")]

time_stop=time.time()                                                                  # by AI 
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
print("Accuracy : ", 100-(total_miss//total_char*100),' %',sep='')
print("Words Per Minute(WPM) [avg:-40 wpm] : ",int(((total_char-total_miss)/time_taken)*60)," WPM",sep='')
