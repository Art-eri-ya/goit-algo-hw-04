def parse_input(user_input):
    cmd, *args = user_input.split(" ")
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added successfully!"
    except ValueError:
        return "The provided data is not enough for adding a new contact"

def change_contact(args, contacts):
    if len(args) < 2:
        return "Please provide name and new phone number."
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated successfully!"
    else:
        return f"There is no contact with name: '{name}'"

def show_phone(args, contacts):
    if not args:
        return "Please enter the name of the contact"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"There is no contact with name: '{name}'"

def show_all(args, contacts):
    return contacts


def main ():
    contacts = {}
    print("Hey, I'm your assistant bot!")
    while True:
        command = input("Enter your command: ").strip().lower()
        command, *args = parse_input(command)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("I don't know what you mean.")

if __name__ == "__main__":
    main()