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
    print('Enter contact name and phone with space: ')
    contact_info = input().split()
    contact_name = contact_info[0]
    contact_phone = contact_info[1]
    contacts[contact_name] = contact_phone
    return "Contact added successfully"

@input_error
def handle_change():
    print('Enter contact name you want to change and new phone with space: ')
    contact_info = input().split()
    contact_name = contact_info[0]
    contact_phone = contact_info[1]
    contacts[contact_name] = contact_phone
    return "Contact phone number updated successfully"

@input_error
def handle_phone():
    print('Enter contact name:')
    contact_name = input()
    contact_phone = contacts[contact_name]
    return f"Phone number for {contact_name}: {contact_phone}"

@input_error
def handle_show_all():
    output = "Contacts:\n"
    for contact_name, contact_phone in contacts.items():
        output += f"{contact_name}: {contact_phone}\n"
    return output.strip()

def parse_command(command):
    command = command.lower()
    if 'hello' in command:
        return handle_hello
    elif 'add' in command:
        return handle_add
    elif 'change' in command:
        return handle_change
    elif 'phone' in command:
        return handle_phone
    elif 'show all' in command:
        return handle_show_all
    elif 'good bye' in command or 'close' in command or 'exit' in command:
        return exit
    else:
        return None

def main():
    while True:
        command = input('Enter a command:')
        command_handler = parse_command(command)

        if command_handler is None:
            print('Unknown command!')
            continue

        if command_handler == exit:
            print('Good bye!')
            break

        response = command_handler()
        print(response)

main()
