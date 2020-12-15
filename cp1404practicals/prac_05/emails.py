def main():
    email = input("Email: ")
    email_dict = {}
    while email.isspace() is False or email != "":
        name = email.split("@")[0]
        answer = input("Is your name {}? (Y/N)".format(name)).upper()
        if answer == "Y" or "YES":
            email_dict[name] = email
        elif answer == "N" or "NO":
            name = input("Name: ")
            email_dict[name] = email
        email = input("Email: ")

    for dict_name, dict_email in email_dict.items():
        print("{} ({})")



main()