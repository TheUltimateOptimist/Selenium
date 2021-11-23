class WebsiteData:
    @staticmethod
    def combination_link(indices:tuple[int]) -> str:
        search_word = ""
        for index in indices:
            search_word+=chr(index + 97)
        return f"https://www.gelbeseiten.de/Suche/{search_word}/Deutschland"
    