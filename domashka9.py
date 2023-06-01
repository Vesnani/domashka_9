def main():
    contacts = {}

    def input_error(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except KeyError:
                return "Contact not found"
            except ValueError:
                return "Invalid input"
            except IndexError:
                return "Invalid input"
        return wrapper

    @input_error
    def handle_hello():
        return "How can I help you?"

    @input_error
    def handle_add():
        contact_name = input('Enter contact name: ')
        contact_phone = input('Enter contact phone: ')
        contacts[contact_name] = contact_phone
        return "Contact added successfully"

    @input_error
    def handle_change():
        contact_name = input('Enter contact name you want to change: ')
        if contact_name in contacts:
            contact_phone = input('Enter new contact phone: ')
            contacts[contact_name] = contact_phone
            return "Contact phone number updated successfully"
        else:
            return "Contact not found"

    @input_error
    def handle_phone():
        contact_name = input('Enter contact name: ')
        contact_phone = contacts.get(contact_name, "Contact not found")
        return f"Phone number for {contact_name}: {contact_phone}"

    @input_error
    def handle_show_all():
        if not contacts:
            return "No contacts found."
        output = "Contacts:\n"
        for contact_name, contact_phone in contacts.items():
            output += f"{contact_name}: {contact_phone}\n"
        return output.strip()

    COMMANDS = {
        'hello': handle_hello,
        'add': handle_add,
        'change': handle_change,
        'phone': handle_phone,
        'show all': handle_show_all,
        'good bye': exit,
        'close': exit,
        'exit': exit,
    }

    def parse_command(command):
        command = command.lower()

        for words in COMMANDS.keys():
            if words in command:
                return COMMANDS[words]

        return None

    while True:
        command = input('Enter a command: ')
        command_handler = parse_command(command)

        if command_handler is None:
            print('Unknown command!')
            continue

        if command_handler == exit:
            print('Good bye!')
            break

        response = command_handler()
        print(response)

if __name__ == '__main__':
    main()
