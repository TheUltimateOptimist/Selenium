import fundamentals as f

indexList = []


def writeWitz(index):
    print(index)
    witz = f.findElement(
        f"/html/body/div[1]/div[3]/div[1]/div/blockquote[{str(index)}]/p", "x-path").text
    print(witz)
    if witz != "":
        file.write(witz + "\n")
        return True
    else:
        return False


f.openAnyWebsite("https://www.witzepause.com/akademiker-witze")
file = open("akademiker.txt", "a", encoding="utf-8")
for i in range(1, 41):
    if writeWitz(i) == False:
        indexList.append(i)
while len(indexList) > 0:
    for index in indexList:
        if writeWitz(i) == True:
            indexList.remove(i)
