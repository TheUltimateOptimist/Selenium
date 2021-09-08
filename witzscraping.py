import fundamentals as f

indexList = []


def writeWitz(index, file):
    print(index)
    if index == 2:
        return True
    else:
        witz = f.findElement(
            f"/html/body/div[1]/div[3]/div[1]/div/blockquote[{str(index)}]/p", "x-path").text
        print(witz)
        if witz != "":
            file.write(witz + "\n")
            return True
        else:
            return False


def removeDoubleLines():
    realFile = open("allekinder.txt", "r")
    lines = realFile.readlines()
    witze = []
    print("Lines: " + str(lines))
    for line in lines:
        if witze.__contains__(line) == False:
            witze.append(line)
    file = open("allekinder-kategorie.txt", "a")
    print("witze: " + str(witze))
    for witz in witze:
        file.write(witz)


f.openAnyWebsite("https://www.witzepause.com/alle-kinder-sprueche?page=4")
file = open("allekinder.txt", "a", encoding="utf-8")
try:
    for i in range(1, 200):
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
removeDoubleLines()
