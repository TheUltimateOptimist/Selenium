#from sales_email import SalesEmail
import sql
import time

class EmailBot:
    def __init__(self, number_of_emails, delay = 4) -> None:
        self.number_of_emails = number_of_emails
        self.delay = delay
    def __get_v_card(self, adress:str, id:int):
        return f"BEGIN:VCARD\nVERSION:3.0\nEMAIL;TYPE=work:{adress}\nFN:{str(id)}\nPRODID:-//Open-Xchange//7.10.4-Rev27//EN\nREV:2021-11-26T00:03:29Z\nEND:VCARD\n"

    def __get_number_of_sent_emails(self) -> int:
        return int(sql.execute("SELECT COUNT(*) FROM requests")[0][0])

    def __get_destination_addresses(self) -> list:
        sent_emails = self.__get_number_of_sent_emails()
        addresses = sql.execute(f"SELECT company_email from scraped_companys WHERE company_id > {sent_emails} and company_id <= {sent_emails + self.number_of_emails}")
        result = []
        for address in addresses:
            result.append(str(address[0]))
        return result

    def produce_contacts(self):
        with open("contacts.txt", "a") as file:
            for i,address in enumerate(self.__get_destination_addresses()):
                file.write(self.__get_v_card(adress=address, id=i))

EmailBot(100).produce_contacts()
            


    
        
