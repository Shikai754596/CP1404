def main():
    text = input("Text: ")
    text_List = text.split()
    text_dictionary = {}
    for char in text_List:
        text_dictionary[char] = text_dictionary.get(char, 0) + 1
    width = len(sorted(text_dictionary.items(), reverse=True)[0][0])
    for word, number in text_dictionary.items():
        print("{:{}} : {}".format(word, width, number))


main()
