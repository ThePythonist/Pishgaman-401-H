def main():
    def register():
        username = input("Choose a username : ").lower()
        password = input("Choose a password : ")

        open("users.txt", "a+").write(username + "\n")
        open("passwords.txt", "a+").write(password + "\n")

        print(f"Registered user {username}")

    def login():
        users = [i[:-1] for i in open("users.txt").readlines()]
        passwords = [i[:-1] for i in open("passwords.txt").readlines()]
        accounts = dict(zip(users, passwords))

        username = input("Enter your username : ").lower()
        password = input("Enter your password : ")

        if username in accounts:
            if accounts[username] == password:
                print("Successfully logged in")
            else:
                print("Password is incorrect")
        else:
            print("User not found")
            main()

    entry = input("""
Choose an option :
1 : Register
2 : Login to your account
: """)

    if entry == "1":
        register()
    elif entry == "2":
        login()
    else:
        print("Invalid input. Choose 1 or 2")
        main()


main()
