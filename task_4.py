from colorama import Fore

def log_base(message):
    print(f"{Fore.BLUE}{message}{Fore.RESET}")

def log_answer(message):
    print(f"{Fore.GREEN}{message}{Fore.RESET}")

def log_error(message):
    print(f"{Fore.RED} [ERROR] {message} {Fore.RESET}")

contacts = {}

def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return log_error("Enter correct name and phone please.")
        except IndexError:
            return log_error("Enter correct name.")
        except KeyError:
            return log_error("This contact does not exist.")

    return inner

@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args):
    name, phone = args
    contacts[name] = phone    
    return "Contact updated."

@input_error
def show_phone(args):
    name = args[0]
    return contacts[name]

def show_all():
    if not contacts:
        return "No contacts saved."
    
    result = "Contact list:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def main():
    log_base("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            log_answer("Good bye!")
            break
        elif command == "hello":
            log_answer("How can I help you?")
        elif command == "add":
            log_answer(add_contact(args))
        elif command == "change":
            log_answer(change_contact(args))
        elif command == "phone":
            log_answer(show_phone(args))
        elif command == "all":
            log_answer(show_all())
        else:
            log_error("Invalid command.")

if __name__ == "__main__":
    main()