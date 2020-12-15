def main():
    text = input("Text: ")
    text_List = text.split()
    text_dictionary = {}
    for char in text_List:
        text_dictionary[char] = text_dictionary.get(char, 0) + 1
    width_list = []
    for y in range(len(sorted(text_dictionary))):
        width_list.append(len(sorted(text_dictionary)[y]))
    width = max(width_list)
    for word, number in text_dictionary.items():
        print("{:{}} : {}".format(word, width, number))


main()
