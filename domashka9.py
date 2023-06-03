contacts = {}

def input_error(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except KeyError:
            return 'Wrong name'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'Pls print: name and number'
        except TypeError:
            return 'Wrong command.'

    return wrapper

@input_error
def hello_func():
    return 'How can I help you?'

@input_error
def exit_func():
    return 'good bye'

@input_error
def add_func(data):
    name, phone = create_data(data)

    if name in contacts:
        raise ValueError('This contact already exists.')
    contacts[name] = phone
    return f'You added a new contact: {name} with this {phone}.'

@input_error
def change_func(data):
    name, phone = create_data(data)
    if name in contacts:
        contacts[name] = phone
        return f'You changed the number to {phone} for {name}.'
    return 'Use the add command, please.'

@input_error
def search_func(name):
    if name.strip() not in contacts:
        raise ValueError('This contact does not exist.')
    return contacts.get(name.strip())

@input_error
def show_func():
    contacts_list = ''
    for key, value in contacts.items():
        contacts_list += f'{key} : {value} \n'
    return contacts_list

COMMANDS = {
    'hello': hello_func,
    'exit': exit_func,
    'close': exit_func,
    'good bye': exit_func,
    'add': add_func,
    'change': change_func,
    'show all': show_func,
    'phone': search_func
}

def change_input(user_input):
    new_input = user_input
    data = ''
    for key in COMMANDS:
        if user_input.strip().lower().startswith(key):
            new_input = key
            data = user_input[len(new_input):]
            break
    if data:
        return reaction_func(new_input)(data)
    return reaction_func(new_input)()

def reaction_func(reaction):
    return COMMANDS.get(reaction, break_func)

def create_data(data):
    new_data = data.strip().split(" ")
    name = new_data[0]
    phone = new_data[1]
    if name.isnumeric():
        raise ValueError('Wrong name.')
    if not phone.isnumeric():
        raise ValueError('Wrong phone.')
    return name, phone

def break_func():
    return 'Wrong enter.'

def main():
    while True:
        user_input = input('Enter command: ')
        if user_input == 'exit' or user_input == 'close' or user_input == 'good bye':
            print('Good bye!')
            break

        result = change_input(user_input)
        print(result)

if __name__ == '__main__':
    main()
