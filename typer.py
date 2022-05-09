import time
from bs4 import BeautifulSoup
import keyboard

PARSER = "html.parser"

def doTyping():
    time.sleep(4)
    soup = BeautifulSoup(getSourceCode(), PARSER)
    words = []
    ui = soup.find("div", id="words")
    for item in ui.children:
        words.append(item.text)
    writeStuff(words[0] + " ")

def writeStuff(text):
    # for letter in text:
    #     if letter != " " and letter.isupper():
    #         keyboard.press_and_release("shift + " + letter)
    #     else:
    #         keyboard.press_and_release(letter)
    #     number = random.randint(1, 8)
    #     time.sleep(number / 100)
    keyboard.write(text)

def getSourceCode():
    with open("text.txt", "r", encoding="utf8") as file:
        code = file.read()
        # code.replace("\n", "")
        return code
    
    
    