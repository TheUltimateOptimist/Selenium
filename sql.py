#from mysql.connector import connect, Error
def execute(sqloperation):
    """
    param1: String sqloperation -> sql operation to execute
    param2: Boolean showOperation -> should it print the sql operation
    connects to personal_database and executes the given sql operation returning the query result
    prints the sql operation if showOperation = True
    """
    with open("emails.txt", "a") as e:
        e.write(sqloperation + "\n")
    # try:
    #     with connect(
    #             host="localhost",
    #             user="root",
    #             password="A1a1B2b2",
    #             database="companys"
    #     ) as connection:
    #         cursor = connection.cursor()
    #         cursor.execute("SET SQL_SAFE_UPDATES = 0")
    #         cursor.execute(sqloperation)
    #         result = cursor.fetchall()
    #         connection.commit()
    #         return result
    # except Error as e:
    #     print(e)