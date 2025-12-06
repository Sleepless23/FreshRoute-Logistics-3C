from user import auth, add_user
from modules.admin_menu import admin_menu
from modules.dispatcher_menu import dispatcher_menu
from modules.driver_menu import driver_menu

def register():
    print(f"\n\033[44mREGISTER STAFF ACCOUNT\033[0m\n{'-' * 80}")
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    confirm_pass = input("Enter confirm password: ")
    
    if password != confirm_pass:
        print("Password and Confirmed aren't the same!\n")
        return
    
    print(f"\nSelect role:\n{'-' * 80}")
    register_menu = ['Admin', 'Dispatcher', 'Driver']
    for i, r in zip(range(4), register_menu):
        print(f"{i + 1}. {r}")
    
    role_input = int(input("Role: "))

    # lance: (minor debug) removed color coding, interferes with role checking in the json data file.
    roles = {
        1: "admin",
        2: "dispatcher", 
        3: "driver"
    }
    
    if role_input not in roles:
        print("\033[31mInvalid role selected.\033[0m\n")
        return
    
    role = roles[role_input]
    
    # lance: (minor change) fixed the color coding, was displaying incorrectly.
    if add_user(username, password, role):
        print("\033[32mAccount created successfully!\033[0m\n") 
    else:
        print("Username is taken!\n")
        
def login():
    print(f"\n\033[42mLOGIN\033[0m\n{'-' * 80}")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    user = auth(username, password)
    
    if not user:
        print("Invalid credentials.\n")
        return None
    
    print(f"\nWelcome, \033[92m{user.username}\033[0m! (Role: \033[95m{user.role}\033[0m)")
    return user

def main():
    while True:
        print(f"\n\033[43mFreshRoute Logistics System\033[0m\n{'-' * 80}")
        login_menu = ['\033[32mLogin\033[0m', '\033[34mRegister\033[0m', '\033[31mExit\033[0m']
        for i, m in zip(range(4), login_menu):
            print(f"{i + 1}. {m}")
        
         # lance: (minor change) removed int conversion to handle non-integer error handling + strip().
        choice = input(f"{'-' * 80}\nEnter your choice: ").strip()

        # lance (minor change) added an if statement for error handling - prevents the program from crashing.
        if choice == "":
            print("\nNo input detected. Please enter a number.\n")
            continue

        if not choice.isdigit():
            print("\nInvalid input. Please enter a valid number.\n")
            continue
        
        match choice:
            case 1:
                user = login()
                if not user:
                    continue
                match user.role:
                    case "admin":
                        admin_menu(user)
                    case "dispatcher":
                        dispatcher_menu(user)
                    case "driver":
                        driver_menu(user)        
            case 2:
                register()
            case 3:
                print("Bye-bye!")
                break
            case _:
                print("Invalid choice.\n")
            
if __name__ == "__main__":
    main()