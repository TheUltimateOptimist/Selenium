from scraper import Scraper
from scrape_state import ScrapeState
class EmailExtractor:
    BREAK_LIST = ['"', "/", "}", "{", "]", "[", "}", "\\", "'", "'", ",", ";", " ", ":", "?"]
    def __init__(self, scraper_state:ScrapeState, articles:list[str]) -> None:
        self.scraper_state = scraper_state
        self.articles = articles
    
    def __save_email(self, email:str) -> None:
        with open("scraped_emails.txt", "a") as emails_file:
            emails_file.write(email + "\n")
        self.scraper_state.increase_found_emails()

    def __extract_article_email(self, article_text:str, index:int) -> None:
        email_found = False
        for i, letter in enumerate(article_text):
            if letter == "@":
                email_found = True
                email = "@"
                n = i - 1
                while article_text[n] not in self.BREAK_LIST:
                    email = article_text[n] + email     
                    if n == 0:
                        break 
                    n-=1
                n = i + 1
                while article_text[n] not in self.BREAK_LIST:
                    email+=article_text[n]
                    if n == len(article_text) - 1:
                        break   
                    n+=1
                break
        if email_found:
            self.__save_email(email)
        else:
            print(index)
            self.scraper_state.increase_unfound_emails()

    def extract_all_emails(self):
        for i,article in enumerate(self.articles):
            self.__extract_article_email(article, i)




        
        





    


