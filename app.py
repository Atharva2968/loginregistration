users = {}

def register():
    print("\n--- Register ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        print("User already exists!")
    else:
        users[username] = password
        print("Registration successful!")

def login():
    print("\n--- Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful! Welcome", username)
    else:
        print("Invalid username or password")

while True:
    print("\n===== User Authentication System =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice")
