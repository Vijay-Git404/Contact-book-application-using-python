contact_book={} #first we create the dictionary
def display_menu():                    # Create function to display options
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")
def add_contact(contact_book):    # Create functions for all options
    name = input("Enter name:").strip()
    phone = input("Enter phone:")
    email = input("Enter email:")
    address = input("Enter address:")
    if name in contact_book:
        print("Contact already exists!")
    else:
        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")
def view_contact(contact_book):
    name=input("Enter Name:")
    if name in contact_book:
        print("Name:",name)
        print("Phone:",contact_book[name]["phone"])
        print("email:",contact_book[name]["email"])
        print("address:",contact_book[name]["address"])
    else:
        print("Contact not found!")
def edit_contact(contact_book):
    name=input("Enter Name of contact to update:").strip()
    if name in contact_book:
        phone=input("Enter new phone:")
        email=input("Enter new email:")
        address=input("Enter new address")
        if phone!='':
            contact_book[name]["phone"]=phone
        if email!='':
            contact_book[name]["email"]=email
        if address!='':
            contact_book[name]["address"]=address
        print("Contact updated succesfully!")
    else:
        print("Contact not found!")
def delete_contact(contact_book):
    name=input("Enter name of contact  to delete:")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")
while True:                    #use while loop to execute the program.
    display_menu()
    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_contact(contact_book)

    elif choice == 2:
        view_contact(contact_book)

    elif choice == 3:
        edit_contact(contact_book)

    elif choice == 4:
       delete_contact(contact_book)
    elif choice == 5:
        print(contact_book)

    elif choice == 6:
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
