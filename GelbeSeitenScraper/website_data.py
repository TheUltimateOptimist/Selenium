class WebsiteData:
    @staticmethod
    def combination_link(indices:tuple, postleizahlen_mode:bool) -> str:
        search_word = ""
        if not postleizahlen_mode:
            for index in indices:
                search_word+=chr(index + 97)
            return f"https://www.gelbeseiten.de/Suche/{search_word}/Deutschland"
        else:
            for index in indices:
                search_word+=str(index)
            return f"https://www.gelbeseiten.de/Suche/k/{search_word}"
    