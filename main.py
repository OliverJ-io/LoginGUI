from password_utils import *

running = True
filename = "passwords.csv"

while running:
    print(f"Welcome Please select a option\n(1)Create account\n(2)Login\n(3)Exit\n(4)Admin")
    prompt_option = input(": ")
    if prompt_option == "1":
        username = input("Username: ")
        password = input("Password: ")
        is_admin = input("Admin (Y/N): ")
        save_password(username, password, is_admin, filename)
    elif prompt_option == "2":
        username = input("Username: ")
        password = input("Password: ")
        if read_file(filename, username)['PASSWORD'] == hash_password(password):
            print(f"Hello {username}")
        else:
            print("Incorrect password or username")
    elif prompt_option == "3":
        running = False
    elif prompt_option == "4":
        username = input("Username: ")
        password = input("Password: ")
        if read_file(filename, username)['PASSWORD'] == hash_password(password) and read_file(filename, username)['ADMIN']:
            print("You Are Admin")
        else:
            print("You Are Not A Admin")
            pass