from random import shuffle
from email_provider import WichtelEmail
from time import sleep

def listsEqual(participants, workingList):
    for i,name in enumerate(participants):
        if name == workingList[i]:
            return True
    return False

emails = ["odilliaunger@baustoffhandel-dueck.de","ungermike2002@gmail.com", "ducklisamarie@gmail.com", "jonathan.dueck@digital-confidence.de", "info@baustoffhandel-dueck.de"]
participants = ["Odillia", "Mike", "Lisa", "Jonathan", "Amelie"]
workingList = ["Odillia", "Mike", "Lisa", "Jonathan", "Amelie"]
while listsEqual(participants, workingList):
    shuffle(workingList)
for i,name in enumerate(participants):
    #print(name, " hat ", workingList[i], " gezogen")
    WichtelEmail(emails[i], f"Wichteln {name}", f"Herzlichen Glückwunsch!!\nDu hast {workingList[i]} gezogen").send()
    print(name, " received email")
    sleep(7)

