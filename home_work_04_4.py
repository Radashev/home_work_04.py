
def parse_input(user_input):
    """
    Функція розбирає введений користувачем рядок на команду та її аргументи.
    """
    parts = user_input.split()
    command = parts[0].lower()  # перша частина рядка - команда
    args = parts[1:]  # решта частин рядка - аргументи
    return command, args

def add_contact(contacts, name, phone_number):
    """
    Додає контакт в словник.
    """
    contacts[name] = phone_number
    print("Contact added.")

def change_contact(contacts, name, new_phone_number):
    """
    Змінює номер телефону для вказаного імені.
    """
    if name in contacts:
        contacts[name] = new_phone_number
        print("Contact updated.")
    else:
        print("Contact not found.")

def show_phone(contacts, name):
    """
    Показує номер телефону для вказаного імені.
    """
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

def show_all(contacts):
    """
    Показує всі контакти.
    """
    if contacts:
        for name, phone_number in contacts.items():
            print(f"{name}: {phone_number}")
    else:
        print("No contacts found.")

def main():
    """
    Основна функція, що управляє циклом обробки команд.
    """
    contacts = {}
    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)
        
        if command == "exit" or command == "close":
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                add_contact(contacts, args[0], args[1])
            else:
                print("Invalid arguments. Usage: add [name] [phone_number]")
        elif command == "change":
            if len(args) == 2:
                change_contact(contacts, args[0], args[1])
            else:
                print("Invalid arguments. Usage: change [name] [new_phone_number]")
        elif command == "phone":
            if len(args) == 1:
                show_phone(contacts, args[0])
            else:
                print("Invalid arguments. Usage: phone [name]")
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
