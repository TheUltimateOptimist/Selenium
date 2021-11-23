from scraper import Scraper  

def main():
    platform = input("Enter 'windows' or 'mac': ")
    if platform == "windows":
        Scraper(on_windows=True).scrape()
    elif platform == "mac":
        Scraper(on_windows=False).scrape()
    else:
        main()

if __name__=='__main__':
    main()