import sys

def initial_phone_book():
    rows, cols = int(input("Please enter initial number of contacts: ")), 5
    phone_book = []
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):" % (i + 1))
        print("NOTE: * indicates mandatory fields")
        temp = []
        name = input("Enter name*: ").strip()
        if name == '':
            sys.exit("Name is a mandatory field. Process exiting due to blank field.")
        temp.append(name)
        phone = input("Enter phone number*: ").strip()
        if phone == '':
            sys.exit("Phone number is a mandatory field. Process exiting due to blank field.")
        temp.append(phone)
        email = input("Enter email: ").strip()
        temp.append(email if email else None)
        dob = input("Enter date of birth (dd/mm/yy): ").strip()
        temp.append(dob if dob else None)
        category = input("Enter category (family/friends/work/others): ").strip()
        temp.append(category if category else None)
        phone_book.append(temp)
    return phone_book

def add_contact(pb):
    print("\nAdd New Contact:")
    temp = []
    name = input("Enter name*: ").strip()
    if name == '':
        print("Name is mandatory.")
        return
    temp.append(name)
    phone = input("Enter phone number*: ").strip()
    if phone == '':
        print("Phone number is mandatory.")
        return
    temp.append(phone)
    email = input("Enter email: ").strip()
    temp.append(email if email else None)
    dob = input("Enter date of birth (dd/mm/yy): ").strip()
    temp.append(dob if dob else None)
    category = input("Enter category (family/friends/work/others): ").strip()
    temp.append(category if category else None)
    pb.append(temp)
    print("Contact added successfully!")

def remove_contact(pb):
    name = input("Enter the name of the contact to remove: ").strip()
    for contact in pb:
        if contact[0].lower() == name.lower():
            pb.remove(contact)
            print("Contact removed successfully!")
            return
    print("Contact not found.")

def delete_all_contacts(pb):
    pb.clear()
    print("All contacts deleted.")

def search_contact(pb):
    name = input("Enter the name to search: ").strip()
    found = False
    for contact in pb:
        if contact[0].lower() == name.lower():
            print("Contact found:")
            print_contact(contact)
            found = True
    if not found:
        print("Contact not found.")

def display_contacts(pb):
    if not pb:
        print("No contacts to display.")
        return
    print("\nAll Contacts:")
    for contact in pb:
        print_contact(contact)

def print_contact(contact):
    print(f"Name: {contact[0]}")
    print(f"Phone: {contact[1]}")
    print(f"Email: {contact[2]}")
    print(f"DOB: {contact[3]}")
    print(f"Category: {contact[4]}")
    print("-" * 30)

def main():
    print("******************************************************************************")
    print("\t\t\tSMARTPHONE DIRECTORY")
    print("******************************************************************************")
    print("\tyou can now perform the following operations on this phonebook\n")
    print("1. Add new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")

    phone_book = initial_phone_book()

    while True:
        try:
            choice = int(input("\nPlease enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            add_contact(phone_book)
        elif choice == 2:
            remove_contact(phone_book)
        elif choice == 3:
            delete_all_contacts(phone_book)
        elif choice == 4:
            search_contact(phone_book)
        elif choice == 5:
            display_contacts(phone_book)
        elif choice == 6:
            print("Exiting phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()