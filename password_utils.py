import csv, hashlib

PasswordHeaders = ["USERNAME", "PASSWORD", "ADMIN"]
filename = "Data/passwords.csv"

def save_to_file(key, string, is_admin, file):
    with open(file, mode="a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=PasswordHeaders)
        writer.writerow({"USERNAME":key,"PASSWORD":string,"ADMIN":is_admin})
        csvfile.close()

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def save_password(user,password, is_admin):
    if is_admin == "Y":
        admin = True
    elif is_admin == "N":
        admin = False
    elif is_admin == "y":
        admin = True
    elif is_admin == "n":
        admin = False
    else:
        admin = False
    save_to_file(user, hash_password(password), admin, filename)

def read_file(user):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=PasswordHeaders)
        for row in reader:
            if row['USERNAME'] == user:
                return row