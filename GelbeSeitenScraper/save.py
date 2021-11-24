from mysql.connector import connect, Error
def execute(sqloperation):
    """
    param1: String sqloperation -> sql operation to execute
    param2: Boolean showOperation -> should it print the sql operation
    connects to personal_database and executes the given sql operation returning the query result
    prints the sql operation if showOperation = True
    """
    try:
        with connect(
                host="localhost",
                user="root",
                password="A1a1B2b2",
                database="companys"
        ) as connection:
            cursor = connection.cursor()
            cursor.execute("SET SQL_SAFE_UPDATES = 0")
            cursor.execute(sqloperation)
            result = cursor.fetchall()
            connection.commit()
            return result
    except Error as e:
        print(e)


emails = []
for i in range(3):
    with open(f"scraped_emails{i + 1}.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            emails.append(line.split("\n")[0])
emails = list(set(emails))
insert_command = "INSERT INTO scraped_companys VALUES"
for i,email in enumerate(emails):
    insert_command+=f"({i + 1}, '{email}')"
    if i < len(emails) - 1:
        insert_command+=","
execute(insert_command)
