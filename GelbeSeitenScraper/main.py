from scraper import Scraper, PostleizahlScraper  

def main():
    platform = input("Enter 'windows' or 'mac': ")
    if platform == "windows":
        scraper = input("Enter p to scrape postleizahlen c to scrape by combinations: ")
        if scraper == "p":
            PostleizahlScraper(on_windows=True).scrape()
        elif scraper == "c":
            Scraper(on_windows=True).scrape()
    elif platform == "mac":
        scraper = input("Enter p to scrape postleizahlen c to scrape by combinations: ")
        if scraper == "p":
            PostleizahlScraper(on_windows=False).scrape()
        elif scraper == "c":
            Scraper(on_windows=False).scrape()
    else:
        main()

if __name__=='__main__':
    main()