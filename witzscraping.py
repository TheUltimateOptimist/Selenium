import fundamentals as f

indexList = []


def writeWitz(index, file):
    print(index)
    if index == 2:
        return True
    else:
        witz = f.findElement(
            f"/html/body/div[1]/div[3]/div[1]/div/blockquote[{str(index)}]/p", "x-path").text
        witz = " ".join(witz.split("\n"))
        if witz != "":
            file.write(witz + "\n")
            return True
        else:
            return False


def removeDoubleLines(newFilename, oldFilename):
    realFile = open(f"{oldFilename}.txt", "r", encoding="utf-8")
    lines = realFile.readlines()
    witze = []
    print("Lines: " + str(lines))
    for line in lines:
        if witze.__contains__(line) == False:
            witze.append(line)
    file = open(f"{newFilename}.txt", "a", encoding="utf-8")
    print("witze: " + str(witze))
    for witz in witze:
        file.write(witz)


def scrapeJokesOfSite(url, filename):
    f.openAnyWebsite(url)
    file = open(f"{filename}.txt", "a", encoding="utf-8")
    try:
        for i in range(1, 500):
            if writeWitz(i, file) == False:
                indexList.append(i)
    except:
        print("an error ocurred")
    print(indexList)
    while len(indexList) > 0:
        for index in indexList:
            if writeWitz(index, file) == True:
                indexList.remove(index)
                print(indexList)
    file.close()


def scrapeJokesOfAllSites(url, filename):
    try:
        fileLength = 0
        for i in range(1, 200):
            if i > 1:
                addition = f"?page={i}"
            else:
                addition = ""
            scrapeJokesOfSite(url + addition, filename)
            file = open(f"{filename}.txt", "r", encoding="utf-8")
            lines = file.readlines()
            if len(lines) > fileLength:
                fileLength = len(lines)
            else:
                break
    except:
        print("all pages scraped")


def removeLineValues(filename, lineValue):
    file = open(filename, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()
    lines.remove(lineValue)
    newFile = open("new-" + filename, "a", encoding="utf-8")
    for line in lines:
        newFile.write(line)
    import os
    os.remove(filename)
    os.rename("new-" + filename, filename)


listOfCategories = ["akademiker-witze", "alle-kinder-sprueche", "arztwitze", "anwaltswitze", "arbeitswitze", "arztwitze", "bankerwitze", "bauernwitze", "bayern-witze", "beamtenwitze", "blondinenwitze", "boese-witze", "bundeswehr-witze", "buerowitze", "chinesen-witze", "computerwitze", "deine-mutter-witze", "deutsche-witze", "drogen-witze", "familienwitze", "flachwitze", "fussballwitze", "geschichte-witze",
                    "jaegerwitze", "juristen-witze", "kannibalen-witze", "kellnerwitze", "kinderwitze", "laenderwitze", "musikerwitze", "oesterreicher-witze", "ostfriesenwitze", "polenwitze", "politiker-witze", "polizei-witze", "schlechte-witze", "schulwitze", "sportwitze", "studentenwitze", "tierwitze", "urlaubswitze", "weihnachtswitze", "wortwitze"]
# print(len(listOfCategories))
# for category in listOfCategories:
#     scrapeJokesOfAllSites(f"https://www.witzepause.com/{category}", category)
#     removeDoubleLines(f"{category}-kategorie", f"{category}")

for category in listOfCategories:
    with open(f"gescrapteWitze/{category}-kategorie.txt", "r", encoding="utf-8") as readfile:
        number = len(readfile.readlines())
        with open(f"gescrapteWitze/1. witze-info.txt", "a", encoding="utf-8") as writeFile:
            writeFile.write(category + ": " + str(number) + "\n")
