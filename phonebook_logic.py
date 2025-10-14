"""
Storage operations
1. loadDataFromStorage, 2. saveDataInStorage
"""
#1. Load data from database
def loadDataFromStorage(database) :
    contacts = {}
    try:
        with open(database,"r") as file : 
            for line in file :
                line.strip()
                if not line or ":" not in line :
                    break
                else:name,number = line.split(":")
                contacts[name] = number    
    except FileNotFoundError : pass
    return contacts

#2. Save data in the storage
def saveDataInTheStorage(contacts,database):
    try:
        with open(database, "w") as file :
            for name,number in contacts.items():
                file.write(f"{name} : {number} \n") 
    except FileNotFoundError : pass
"""
User operations
1.addContact, 2.deleteContact, 3.seeAllContacts, 4.removeAllContacts, 5.changeContactPhonenumber
"""
#1. Add new contact in the phonebook.
def addContact (contacts,name,number) :
    contacts = contacts.update({name : number})
    

#2. Delete contact from phonebook.
def deleteContact(contacts,name) :
    contacts = contacts.pop(name)
    

#3. See all contacts from phonebook
def seeAllContacts(contacts) :
    for x, y in contacts.items() :
        print(x,y)

#4.  Remove all contacts from phonebook
def removeAllContacts(contacts) :
    contacts.clear()
    

#5. Change Contact Phonenumber
def changeContactPhonenumber(contacts,name,newNumber) :
    contacts[name] = newNumber
    


