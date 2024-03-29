import sys

from PyQt6.QtWidgets import QApplication
from PyQt6 import uic
from password_utils import *
from group_utils import *

isLoggedIn = False
LoggedInUser = ""

def open_admin_panel():
    global LoggedInUser, isLoggedIn
    if isLoggedIn and read_file(LoggedInUser)["ADMIN"] == 'True':
        admin_panel.show()
    else:
        pass

def open_change_password():
    change_password.show()

def open_change_username():
    change_username.show()

def open_create_account():
    create_account.show()

def create_account_action():
    username = create_account.username_input.text()
    password = create_account.password_input.text()
    save_password(username, password, "N")
    create_account.username_input.setText("")
    create_account.password_input.setText("")
    create_account.hide()

def open_force_logout():
    force_logout.show()

def open_get_admins():
    get_admins.show()

def open_get_passwords():
    get_passwords.show()

def back_admin_panel():
    admin_panel.hide()

def open_login():
    login.show()

def login_action():
    global isLoggedIn, LoggedInUser
    username = login.username_input.text()
    password = login.password_input.text()
    if read_file(username)['PASSWORD'] == hash_password(password):
        login.username_input.setText("")
        login.password_input.setText("")
        isLoggedIn = True
        LoggedInUser = username
        login.hide()

def open_message_user():
    message_user.show()

def open_remove_account():
    remove_account.show()

def open_set_admin():
    set_admin.show()

def open_use_hash():
    use_hash.show()

def exit():
    app.exit(0)

def load_buttons():
    #Home Buttons
    home.admin.clicked.connect(open_admin_panel)
    home.login.clicked.connect(open_login)
    home.create_account.clicked.connect(open_create_account)
    home.exit.clicked.connect(exit)

    #Admin Panel Buttons
    admin_panel.back.clicked.connect(back_admin_panel)
    admin_panel.set_admin.clicked.connect(open_set_admin)
    admin_panel.get_admins.clicked.connect(open_get_admins)
    admin_panel.change_password.clicked.connect(open_change_password)
    admin_panel.get_passwords.clicked.connect(open_get_passwords)
    admin_panel.use_hash.clicked.connect(open_use_hash)
    admin_panel.force_logout.clicked.connect(open_force_logout)
    admin_panel.remove_account.clicked.connect(open_remove_account)
    admin_panel.login.clicked.connect(open_login)
    admin_panel.change_username.clicked.connect(open_change_username)
    admin_panel.message_user.clicked.connect(open_message_user)
    #admin_panel.block_user.clicked.connect(open_block_user)
    #admin_panel.get_features.clicked.connect(open_get_features)
    #admin_panel.set_features.clicked.connect(open_set_features)
    #admin_panel.ban_user.clicked.connect(open_ban_user)
    #admin_panel.get_banned_users.clicked.connect(open_get_banned_users)
    #admin_panel.force_password_reset.clicked.connect(open_force_password_reset)
    #admin_panel.get_permissions.clicked.connect(open_get_permissions)
    #admin_panel.set_permissions.clicked.connect(open_set_permissions)
    #admin_panel.get_groups.clicked.connect(open_get_groups)
    #admin_panel.set_group.clicked.connect(open_set_group)
    #admin_panel.add_group.clicked.connect(open_add_group)
    #admin_panel.kick_user.clicked.connect(open_kick_user)
    #admin_panel.ban_user_group.clicked.connect(open_ban_user_group)
    admin_panel.exit.clicked.connect(exit)

    # Login Buttons
    login.login.clicked.connect(login_action)

    #Create Account Buttons
    create_account.create_account.clicked.connect(create_account_action)

def loadUi(filename:str):
    return uic.loadUi(f'UI_Files/{filename}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin_panel = loadUi('admin_panel.ui')
    change_password = loadUi('change_password.ui')
    change_username = loadUi('change_username.ui')
    create_account = loadUi('create_account.ui')
    force_logout = loadUi('force_logout.ui')
    get_admins = loadUi('get_admins.ui')
    get_passwords = loadUi('get_passwords.ui')
    home = loadUi('home.ui')
    login = loadUi('login.ui')
    message_user = loadUi('message_user.ui')
    remove_account = loadUi('remove_account.ui')
    set_admin = loadUi('set_admin.ui')
    use_hash = loadUi('use_hash.ui')
    load_buttons()
    home.show()
    sys.exit(app.exec())