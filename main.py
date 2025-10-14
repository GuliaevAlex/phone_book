import phonebook_logic as pbl

def main():
    database = "data.txt"
    contacts = pbl.loadDataFromStorage(database)

    while True :
        print("\n---Phone Book--- \n"
        "1. Show all contacts  \n"
        "2. Add contact  \n"
        "3. Change contact phonenumber  \n"
        "4. Delete contact\n"
        "5. Delete all contacts\n"
        "6. Save data in storage\n"
        "7. Save & Exit  \n" )

        userChoise = input("Choose operation: ")    
        if userChoise == "1":
            pbl.seeAllContacts(contacts)
        elif userChoise == "2":
            name = input("Enter name: ")
            number = input("Enter number: ")
            pbl.addContact(contacts,name, number)
        elif userChoise =="3":
            name = input("Enter name: ")
            number = input("Enter new number: ")
            pbl.changeContactPhonenumber(contacts,name,number)
        elif userChoise =="4":
            name = input("Enter name: ")
            warning = input("You realy want delete this contact? Y/N ")
            if warning.upper() =="Y":
                pbl.deleteContact(contacts,name)
            elif warning.upper() =="N":
                print()
            else: print("Invalid input")
        elif userChoise == "5":
            pbl.removeAllContacts(contacts)
        elif userChoise == "6":
            pbl.saveDataInTheStorage(contacts,database)
        elif userChoise == "7":
            pbl.saveDataInTheStorage(contacts,database)
            break
        else:
            print("Invalid operation")

if __name__ == "__main__":
    main()
