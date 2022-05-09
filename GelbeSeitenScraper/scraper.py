import time
from base_converter import BaseConverter
from bs4 import BeautifulSoup
from email_extractor import EmailExtractor
from website_data import WebsiteData
from scrape_state import ScrapeState
from selenium import webdriver
from sql import execute
class Scraper:
    # location of the chrome webdriver
    PATH_MAC = "/Users/jonathandueck/Desktop/chromedriver"
    PATH_WINDOWS = "C:\AppDevelopment\chromedriver.exe"
    PARSER = "html.parser"
    NUMBER_OF_LETTERS = 4

    def __init__(self, on_windows=True) -> None:
        self.state = None
        self.driver = webdriver.Chrome(self.PATH_WINDOWS) if on_windows else self.PATH_MAC
        self.site = None

    def open_website(self, indices:tuple, postleizahlen_mode=False) -> None:
        consecutive_fails = 0
        try:
            self.driver.get(WebsiteData.combination_link(indices, postleizahlen_mode))
            self.site = BeautifulSoup(self.driver.page_source, self.PARSER)
            consecutive_fails = 0
        except:
            consecutive_fails+=1
            if consecutive_fails == 3:
                self.driver.quit()
            time.sleep(3)
            self.open_website(indices)

    def get_articles(self) -> list:
        articles = self.site.find_all("article")
        for i, article in enumerate(articles):
            articles[i] = str(article)
        # if len(articles) != self.__get_number_of_articles():
        #     raise ValueError("retrieved articles do not include all found articles")
        return articles

    def get_number_of_articles(self):
        number = int(str(self.site.find("span", id="mod-TrefferlisteInfo")).split('">')[1].split("</")[0])
        return number

    def scrape(self):
        self.state = ScrapeState()
        scrape_start_time = time.time()
        completed_combinations = self.state.completed_combinations
        while completed_combinations < 26**self.NUMBER_OF_LETTERS:
            self.open_website(indices=BaseConverter(completed_combinations).to_any_base(number_of_digits=self.NUMBER_OF_LETTERS, specific_base=26), postleizahlen_mode=False)
            EmailExtractor(self.state, self.get_articles()).extract_all_emails()
            self.state.increase_completed_combinations()
            self.state.increase_time_passed(time.time() - scrape_start_time)
            scrape_start_time = time.time()
            completed_combinations+=1


class PostleizahlScraper(Scraper):
    def __init__(self, on_windows=True) -> None:
        super().__init__(on_windows=on_windows)
        with open("completed_combinations.txt", "r") as file:
            self.completed_combinations = int(file.readline().split("\n")[0])

    def __save_postleizahl(self, treffer:int, postleizahl:int):
        execute(f"INSERT INTO postleizahlen(postleizahl, postleizahl_treffer) Values({postleizahl}, {treffer})")
        
    def __combination_completed(self):
        self.completed_combinations+=1
        with open("completed_combinations.txt", "w") as file:
            file.write(str(self.completed_combinations))

    def scrape(self):
        while self.completed_combinations < 10**5:
            postleizahl = BaseConverter(self.completed_combinations).to_any_base(number_of_digits=5, specific_base=10)
            self.open_website(postleizahl, postleizahlen_mode=True)
            error = self.site.find("div", class_="row errorpage-content")
            if error is None:
                self.__save_postleizahl(self.get_number_of_articles(), BaseConverter.tuple_to_decimal_value(postleizahl, 10))
            self.__combination_completed()            

