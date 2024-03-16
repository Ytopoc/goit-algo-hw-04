def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Such a contact already exists, you can change the phone number using the \"change\" "
    contacts[name] = phone
    return "Contact added."
def change_phone(args, contacts):
    name, phone = args
    if name not in contacts:
        return "No contacts found."
    contacts[name] = phone
    return "Contact changed."
def phone_contact(args, contacts):
    name = args[0]
    if name not in contacts:
        return "No contacts found."
    return contacts[name]
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    else:
        result = "Contacts:"
        for name, phone in contacts.items():
            result += f"\n{name}: {phone}"
        return result
 

    



def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello" or command=="hi":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(phone_contact(args,contacts))
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts)) 
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()