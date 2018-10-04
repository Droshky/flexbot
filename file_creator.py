import os
'''
File formats:
    USER DATA: 
        MONEY
        BUSINESSNAME
    CORPORATE DATA: 
        BUSINESSNAME
        NETWORTH
        WORKERAMOUNT/WORKERMAX
        STOCKPRICE
'''


def data_gather(file):
    for line in file:
        return line.split("-")


def remove_files():
    os.rmdir(r"C:\Users\Tyler\PycharmProjects\FLEXBOOT\data\businessdata")
    os.mkdir(r"C:\Users\Tyler\PycharmProjects\FLEXBOOT\data\businessdata")


def add_users(users):
    print(users)
    for user in users:
        os.mkdir(r"C:\Users\Tyler\PycharmProjects\FLEXBOOT\data\businessdata\%s" % user)
        file_name = r"C:\Users\Tyler\PycharmProjects\FLEXBOOT\data\businessdata\%s\user.txt" % user
        file = open(file_name, 'w+')
        file.write("0-none")
        file.close()

def add_user(user):
    os.mkdir(r"C:\Users\Tyler\PycharmProjects\FLEXBOOT\data\businessdata\%s" % user)
    file_name = r"C:\Users\Tyler\PycharmProjects\FLEXBOOT\data\businessdata\%s\user.txt" % user
    file = open(file_name, 'w+')
    file.write("0-none")
    file.close()

def remove_user(user):
    os.remove(r"C:\Users\Tyler\PycharmProjects\FLEXBOOT\data\businessdata\%s" % user)


def create_company(user, company):
    try:
        file_name = r"C:\Users\Tyler\PycharmProjects\FLEXBOOT\data\businessdata\%s\business.txt" % user
        file = open(file_name, 'w+')
        file.write("%s-0-0/5-00.10" % company)
        file.close()
        return "You created: %s" % company
    except:
        print("create_company(%s, %s): NOT VALID" % (user, company))
        return "You cannot create this..."

def add_money(user, money):
    file_name = r"C:\Users\Tyler\PycharmProjects\FLEXBOOT\data\businessdata\%s\user.txt" % user
    file = open(file_name, 'r')
    data = data_gather(file)
    file.close()
    f = open(file_name, 'w')
    f.write("%s-%s" % (int(data[0]+money, data[1])))
    f.close()

def add_bus_net(user, money):
    file_name = r"C:\Users\Tyler\PycharmProjects\FLEXBOOT\data\businessdata\%s\business.txt" % user
    file = open(file_name, 'r')
    data = data_gather(file)
    file.close()
    f = open(file_name, 'w')
    f.write("%s-%s-%s-%s" % (data[0], money, data[2], data[3]))
    f.close()
