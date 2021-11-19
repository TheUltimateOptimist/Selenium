import fundamentals as f

f.openAnyWebsite("https://web.whatsapp.com")
element = f.findElement(
    '/html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[11]', "x-path")
element.click()
