phonebook = {
    "Steve" : "+63-4344-620-292",
    "John" : "+63-2229-748-824",
    "Bob" : "+63-4695-518-188",
    "Vi" : "+63-4550-818-345"
}

def add_contact(name, phone_number):
    phonebook[name] = phone_number

def update_contact(name, phone_number):
    phonebook[name] = phone_number

def view_phonebook():
    print("Current Phonebook")
    for key, value in phonebook.items():
        print(f"{key} : {value}")

while True:
    print("[0] Exit | [1] Add Contact | [2] Update Contact | [3] View Phonebook")
    choice = int(input("Enter the number you want to do: "))

    if choice == 1:
        name = str(input("Enter you name: "))
        phone_number = str(input("Enter your mobile number: "))
        add_contact(name, phone_number)

    elif choice == 2:
        view_phonebook()
        name = str(input("Enter you name: "))
        phone_number = str(input("Enter your mobile number: "))
        update_contact(name, phone_number)

    elif choice == 3:
        view_phonebook()

    elif choice not in {0, 1, 2, 3}:
        print("\nChoice is out of index!")

    else:
        print("Done editing contacts!")
        break