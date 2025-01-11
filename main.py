def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        number_of_words = count_words(file_contents)
        number_of_characters = count_characters(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{number_of_words} words found in the document")
        print()
        for number_of_character in number_of_characters:
            print(f"The '{number_of_character['char']}' character was found {number_of_character['num']} times")
        print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    number_of_characters = {}
    for c in text:
        if not c.isalpha():
            continue
        lower_c = c.lower()
        if lower_c in number_of_characters:
            number_of_characters[lower_c] += 1
        else:
            number_of_characters[lower_c] = 1
    number_of_characters_list = []
    for char, num in number_of_characters.items():
        number_of_characters_list.append({'char': char, 'num': num})
    number_of_characters_list.sort(reverse=True, key=sort_on)
    return number_of_characters_list

def sort_on(dict):
    return dict["num"]

main()