import time
from base_converter import BaseConverter
from bs4 import BeautifulSoup
from email_extractor import EmailExtractor
from website_data import WebsiteData
from scrape_state import ScrapeState
from selenium import webdriver
class Scraper:
    # location of the chrome webdriver
    PATH_MAC = "/Users/jonathandueck/Desktop/chromedriver"
    PATH_WINDOWS = "C:\AppDevelopment\chromedriver.exe"
    PARSER = "html.parser"
    NUMBER_OF_LETTERS = 4

    def __init__(self, on_windows=True) -> None:
        self.state = ScrapeState()
        self.driver = webdriver.Chrome(self.PATH_WINDOWS) if on_windows else self.PATH_MAC
        self.site = None

    def __open_website(self, indices:tuple[int]) -> None:
        try:
            self.driver.get(WebsiteData.combination_link(indices))
            self.site = BeautifulSoup(self.driver.page_source, self.PARSER)
        except:
            time.sleep(10)
            self.__open_website(indices)

    def __get_articles(self) -> list[str]:
        articles = self.site.find_all("article")
        for i, article in enumerate(articles):
            articles[i] = str(article)
        if len(articles) != self.__get_number_of_articles():
            raise ValueError("retrieved articles do not include all found articles")
        return articles

    def __get_number_of_articles(self):
        number = int(str(self.site.find("span", id="mod-TrefferlisteInfo")).split('">')[1].split("</")[0])
        return number if number < 50 else 50

    def scrape(self):
        scrape_start_time = time.time()
        completed_combinations = self.state.completed_combinations
        while completed_combinations < 26**self.NUMBER_OF_LETTERS:
            self.__open_website(indices=BaseConverter(completed_combinations).toBase26(self.NUMBER_OF_LETTERS))
            EmailExtractor(self.state, self.__get_articles()).extract_all_emails()
            self.state.increase_completed_combinations()
            self.state.increase_time_passed(time.time() - scrape_start_time)
            scrape_start_time = time.time()
            completed_combinations+=1

