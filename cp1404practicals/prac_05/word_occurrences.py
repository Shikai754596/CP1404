def main():
    text = input("Text: ")
    text_List = text.split()
    text_dictionary = {}
    for char in text_List:
        text_dictionary[char] = text_dictionary.get(char, 0) + 1
    print(text_dictionary)


main()