WORD_LIST = ["fenster", "tueren", "tuer"]
def get_emails():
    with open("scraped_emails1.txt", "r") as file:
        emails = file.readlines()
        for i, email in enumerate(emails):
            emails[i] = email.split("\n")[0]
        return list(set(emails))

def print_word_occurences(word_list:list[str]):
    for email in get_emails():
        for word in word_list:
            if word in email:
                print(email)

print_word_occurences(WORD_LIST)