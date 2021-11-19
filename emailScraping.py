# import time
import functions
# import fundamentals as f
# properties = ["telefonnummer", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ]
# f.openAnyWebsite("https://www.gelbeseiten.de/Suche/abc/Deutschland")
# try:
#     result = f.findElement("/html/body/div[2]/div[3]/div/div/div[1]/div/div[2]/article[3]", "x-path").get_attribute("data-lazyloaddata")
#     button = f.findElement("/html/body/div[2]/div[3]/div/div/div[1]/div/form/a", "x-path")
# except:
#     result = f.findElement("/html/body/div[3]/div[3]/div/div/div[1]/div/div[2]/article[3]", "x-path").get_attribute("data-lazyloaddata")
#     button = f.findElement("/html/body/div[3]/div[3]/div/div/div[1]/div/form/a", "x-path")
# time.sleep(5)
# for i in range(10000000):
#     print("clicking",i, "------------------------------------------")
#     try:
#         button.click()
#         time.sleep(0.5)
#     except Exception as e:
#         print("ksdjlfsjdklfjl")
#         print(e)
#         break

    
# print(extractPropertie(result, "href", False))
for i in range(26):
    functions.scrapeSite(chr(97 + i))

# /html/body/div[3]/div[3]/div/div/div[1]/div/div[2]/article[1]/div[1]/div/a[2]
# /html/body/div[3]/div[3]/div/div/div[1]/div/div[2]/article[2]/div/div/a[2]

