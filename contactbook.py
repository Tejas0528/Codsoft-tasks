contacts = [] 

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contact = [name, phone]  
    contacts.append(contact)
    print("Contact added!\n")

def view_contacts():
    print("\n--- Contact List ---")
    for contact in contacts:
        print("Name:", contact[0], "| Phone:", contact[1])
    print()

def search_contact():
    name = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print("Found Contact -> Name:", contact[0], "| Phone:", contact[1])
            found = True
            break
    if not found:
        print("Contact not found.\n")

while True:
    print("---- Contact Book ----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
