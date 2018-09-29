import os
import glob


def remove_files():
    mydir = (r"C:\Users\Tyler\PycharmProjects\FLEXBOOT\data\user_bank")
    filelist = [f for f in os.listdir(mydir) if f.endswith(".bak")]
    for f in filelist:
        os.remove(os.path.join(mydir, f))


def add_users(users):
    print(users)
    for user in users:
        print(user)
        try:
            file_name = r"C:\Users\Tyler\PycharmProjects\FLEXBOOT\data\user_bank\bank-%s.txt" % (user)
            file = open(file_name, 'w+')
            file.write("%s-0-None" % (user))
        except UnicodeEncodeError:
            file_name = r"C:\Users\Tyler\PycharmProjects\FLEXBOOT\data\user_bank\bank-UnicodeUsers.txt"
            file = open(file_name, 'a+')
            file.write("%s-0-None-\n")


def add_user(user):
    try:
        file_name = r"C:\Users\Tyler\PycharmProjects\FLEXBOOT\data\user_bank\bank-%s.txt" % (user)
        file = open(file_name, 'w+')
        file.write("%s-0-None" % (user))
    except UnicodeEncodeError:
        file_name = r"C:\Users\Tyler\PycharmProjects\FLEXBOOT\data\user_bank\bank-UnicodeUsers.txt"
        file = open(file_name, 'w+')
        file.write("%s-0-None-\n")


