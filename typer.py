import time
from fundamentals import getPageSourceCode, openAnyWebsite
from bs4 import BeautifulSoup
import keyboard

PARSER = "html.parser"

def extractWords(source_code):
    soup = BeautifulSoup(source_code, PARSER)
    words = []
    ui = soup.find("div", id="words")
    for item in ui.children:
        words.append(item.text)
    
    # with open("text.txt", "w") as file:
    #     file.write("'" + words[0] + " " + "'")
    return words[0] + " "

def writeStuff(text):
    for letter in text:
        keyboard.write(letter)
        time.sleep(1)

def doTyping(delay=10, open_website=True, type_site_url="https://10fastfingers.com/typing-test/german"):
    if open_website:
        openAnyWebsite(type_site_url)
        time.sleep(delay)
    text = extractWords(getPageSourceCode())
    time.sleep(delay)
    keyboard.write(text)
doTyping()
    
    
    