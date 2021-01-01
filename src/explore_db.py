import database

"""
File untuk manajemen database
"""

db = database.Database()

def show():
    datas = db.show()
    print("\nID  |  NAME")
    print('-'*10)
    for ids, name in datas:
        print(str(ids)+"   | "+name)

MENU = """SELECT MENU
[1] Look All Data
[2] Update Existing Data
[3] Delete Data
[4] Quit
        """

while 1:
    print(MENU)
    num_menu = int(input("Select: "))

    if num_menu == 1:
        show()
    elif num_menu == 2:
        ids = int(input("\nInsert ID: "))
        new_name = input("Insert New Name: ")
        db.update_name(ids, new_name)
        print("\nDB Updated!")
        show()
    elif num_menu == 3:
        ids = int(input("\nInsert ID: "))
        db.delete(ids)
        print("\nDB Updated!")
        show()
    elif num_menu == 4:
        db.close()
        break

    continues = input("\nAnother Command (y/n): ")
    if continues.lower() == 'n':
        db.close()
        break

