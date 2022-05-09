from sql import execute
from random import shuffle
emails = []
for i in range(107):
    with open(f"scraped_emails{i + 1}.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            emails.append(line.split("\n")[0])
emails = list(set(emails))
shuffle(emails)
insert_command = "INSERT INTO scraped_companys VALUES"
for i,email in enumerate(emails):
    insert_command+=f"({i + 1}, '{email}')"
    if i < len(emails) - 1:
        insert_command+=","
execute(insert_command)
