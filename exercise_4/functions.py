
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            return 'This contact is already in contacts book'
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return 'Please, enter name and phone'


def change_contact(args, contacts):
    try:
        name, phone = args
        if name not in contacts:
            return 'This person not in your book'
        contacts[name] = phone
        return 'Contact updated.'
    except ValueError:
        return 'Please, enter name and phone'

def show_phone(args, contacts):
    try:
        name = args[0]
        if name not in contacts:
            return 'This person not in your book'
        return f'{name} : {contacts[name]}'
    except ValueError:
        return 'Please, enter name'
    except IndexError:
        return 'Please, enter the name'
    
def show_all(contacts):
    for k,v in contacts.items():
        print(f'{k}:{v}')

