def main():
    email = input("Email: ")
    while email.isspace() is False or email != "":
        name = email.split("@")[0]
        answer = input("Is your name {}? (y/n)".format(name))


main()