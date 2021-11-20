import time
import fundamentals as f
import sql
from auto_email import send
class UnfoundEmails:
    number = 0
    liste = []

def clickToEnd():
    count = 50
    t = time.time()
    try:
        button = f.findElement("/html/body/div[2]/div[3]/div/div/div[1]/div/form/a", "x-path")
    except:
        button = f.findElement("/html/body/div[3]/div[3]/div/div/div[1]/div/form/a", "x-path")
    for i in range(100000005):
        time.sleep(0.6)
        try:
            button.click()
            count+=10
            if count%10000 == 0:
                send("jonathan.dueck@digital-confidence.de", "Email Scraping laoding page", f"{count} eamils successfully loaded")
            t = time.time()
        except Exception as e:
            if time.time() - t > 10:
                send("jonathan.dueck@digital-confidence.de", "Email Scraping reached end of page", f"{count} eamils successfully loaded")
                print(e)
                break

def extractPropertie(text, prop_name, shouldBreak = True):
    if text.__contains__(prop_name):
        prop_name+='":"'
        liste = []
        index = 0
        result = ""
        found = False
        for letter in text:
            if not found and letter == prop_name[index]:
                index += 1
            elif not found and letter != prop_name[index]:
                index = 0
            elif found and letter != '"':
                result+=letter
            elif found and letter == '"' and not shouldBreak:
                found = False
                liste.append(result)
                result = ""
                index = 0
            elif found and letter == '"' and shouldBreak:
                liste.append(result)
                return liste
            if index == len(prop_name):
                found = True
        return liste  
    else:
        return None

def getData(pathList, number):
    for path in pathList:
        try:
            print(path[0])
            print(path[1])
            element =  f.findElement(path, "x-path")
            attribute = element.get_attribute("data-lazyloaddata")
            if attribute is None:
                attribute = element.get_attribute("href")
            return attribute
        except Exception as e:
            #print(e)
            continue
    raise Exception("ELEMENT NOT FOUND ", number)
    

def isNotEqualTo(element, tokenList):
    for token in tokenList:
        if element == token:
            return False
    return True

def extractEmail(pathList, number):
    breakList = ['"', "/", "}", "{", "]", "[", "}", "\\", "'", "'", ",", ";", " ", ":", "?"]
    text = getData(pathList, number)
    if text is None:
        print("email number ", number, " not found")
        UnfoundEmails.number+=1 
        UnfoundEmails.liste.append(number + 1)
        return None
    if not text.__contains__("@"):
        print("email number ", number, " not found")
        UnfoundEmails.number+=1 
        UnfoundEmails.liste.append(number + 1)
    else:
        for i,element in enumerate(text):
            if element == "@":
                email = "@"
                n = i - 1
                while isNotEqualTo(text[n], breakList):
                    email = text[n] + email
                    if n == 0:
                        break
                    n-=1
                n = i + 1    
                while isNotEqualTo(text[n], breakList):
                    email += text[n]
                    n+=1
                    if n == len(text) - 1:
                        break
                return email
    return None

def saveArticleEmail(pathList, number):
    email = extractEmail(pathList, number)
    if email is not None:
        entry = f"INSERT INTO scraped_companys(company_email) VALUES('{email}')"
        sql.execute(email)
    else:
        print("email is none ", number)


def scrapeSite(letter):
    send("jonathan.dueck@digital-confidence.de", "Email Scraping", f"starting work on letter {letter}")
    f.openAnyWebsite(f"https://www.gelbeseiten.de/Suche/{letter}/Deutschland")
    time.sleep(5)
    clickToEnd()
    for i in range(1000000):
        pathList = [f"/html/body/div[3]/div[3]/div/div/div[1]/div/div[2]/article[{i + 1}]", 
                   f"/html/body/div[2]/div[3]/div/div/div[1]/div/div[2]/article[{i + 1}]",
                   f"/html/body/div[3]/div[3]/div/div/div[1]/div/div[2]/article[{i+1}]/div[1]/div/a[2]",
                   f"/html/body/div[2]/div[3]/div/div/div[1]/div/div[2]/article[{i+1}]/div[1]/div/a[2]",
                   f"/html/body/div[3]/div[3]/div/div/div[1]/div/div[2]/article[{i+1}]/div/div/a[2]",
                   f"/html/body/div[2]/div[3]/div/div/div[1]/div/div[2]/article[{i+1}]/div/div/a[2]",]
        try:
            saveArticleEmail(pathList, i)
        except Exception as e:
            print(e)
            print("Unfound Emails: ", UnfoundEmails.number)
            break