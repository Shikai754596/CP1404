def main():
    email = input("Email: ")
    email_dict = {}
    while email != "" and email.isspace() is False:
        name = email.split("@")[0]
        name = " ".join(name.split(".")).title()
        answer = input("Is your name {}? (Y/N) ".format(name)).upper()
        while answer not in "Y N YES NO":
            answer = input("Please choose (Y/N) ".format(name)).upper()
        if answer == "Y" or "YES":
            email_dict[name] = email
        elif answer == "N" or "NO":
            print("pa")
            name = input("Name: ")
            email_dict[name] = email
        email = input("Email: ")

    for dict_name, dict_email in email_dict.items():
        print("{} ({})".format(dict_name, dict_email))


main()
