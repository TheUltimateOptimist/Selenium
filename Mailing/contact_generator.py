from sql import execute
from random import shuffle
import time
class ContactGenerator:
    FILE_PATH = "contacts.vcf"
    def __init__(self, number_of_contacts:int) -> None:
        self.number_of_contacts = number_of_contacts

    def __get_random_emails(self):
        emails = execute("select company_email from scraped_companys inner join requests ON scraped_companys.company_email != requests.request_email")
        result = []
        for email in emails:
            result.append(email[0])
        shuffle(result)
        return result[0 : self.number_of_contacts]

    def __get_v_card(self, adress:str, id:int):
        return f"BEGIN:VCARD\nVERSION:3.0\nEMAIL;TYPE=work:{adress}\nFN:{str(id)}\nPRODID:-//Open-Xchange//7.10.4-Rev27//EN\nREV:2021-11-26T00:03:29Z\nEND:VCARD\n"
        
    def generate(self):
        import os
        if os.path.exists(self.FILE_PATH):
            os.remove(self.FILE_PATH)
        with open(self.FILE_PATH, "a") as file:
            for i, random_email in enumerate(self.__get_random_emails()):
                file.write(self.__get_v_card(random_email, i + 1))
                execute(f"INSERT INTO requests(request_status, request_email, request_time) VALUES(1, '{random_email}', {int(time.time())})")
