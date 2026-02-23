import json # NEW: this help save/load data to files

contacts = {} #create an empty dictionary to store data

# New: function to save contacts to a file
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)
        print("contacts saved!")


# New: function to load contacts from a file
def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
            print("contacts loaded!")
    except FileNotFoundError:
        print("No saved contacts found. Starting with an empty contact book.")
        contacts = {}

# load contacts when the program starts
load_contacts()

# create a menu system
while True:
    print("\n === Contact Book ===")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")
    print("U - Update contact")

    choice = input("chose an option: (1-5): ") 
    if choice == "1":
        name = input("Enter contact name:")
        phone = input("Enter contact phone number:")
        email = input("Enter contact email:")

        contacts[name] = {"phone": phone, "email": email}# contact[] is the key and the value is a dict with the phone and email
        print(f"contact {name} added successfully!")
        save_contacts() # save contacts after adding a new contact

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            for name, info in contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                       
    elif choice == "3":
        search_name = input("Enter contact name to search: ").lower()
        found = False
        for name, info in contacts.items():
            if search_name in name.lower():
                print(f"\nName: {name}")
                print(f"Phone: {info['phone']}")# we us info because the value of the contact is a dict with phone and email, so we can access the phone and email using info, what if we dont use info it will give us and error because it will try to access the phone and email from the contact name which is a string and not a dict.
                print(f"Email: {info['email']}")
                found = True
        if not found:
            print("Contact not found.")

    elif choice == "4":
        delete_name = input("Enter contact name to delete:").lower()
        found = False
        for name in list(contacts.keys()):
            if delete_name in name.lower():
                del contacts[name]
                print(f"Contact {name} deleted successfully!")
                save_contacts() # save contacts after deletion
                found = True
        if not found:
            print("Contact not found.")

    elif choice == "U":
        update_name = input("Enter contact name to update:").lower()
        found = False
        for name in list(contacts.keys()):
            if update_name in name.lower():
                 new_phone = input("Enter new phone number:")
                 new_email = input("Enter new email:")
                 contacts[name] = {"phone": new_phone, "email": new_email}
                 print(f"contact {name} updated successfully")
                 save_contacts()
         
    elif choice == "5":
        print("Existing the contact book. Goodbye!")        
        break




       
                

