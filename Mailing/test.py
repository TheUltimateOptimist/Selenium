teilnehmer = int(input("Teilnehmer: "))
trys = 1000000
liste = []
for i in range(teilnehmer):
    liste.append(i)
from random import shuffle
noMatches = trys
for i in range(trys):
    shuffle(liste)
    for i, number in enumerate(liste):
        if number == i:
            noMatches -=1
            break
    
print("The probability is ", noMatches/trys*100, "%")
    
    