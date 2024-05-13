
def main():
    path = "./books/frankenstein.txt"
    print(f"Begin report of {path}")

    text = get_text_from_file(path)
    counted_words = count_words(text)
    print(f"{counted_words} words found in the document")
    
    counted_letters = count_letters(text)
    print_report(counted_letters)
    
    print("End report")

def get_text_from_file(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_letters(text):
    letter_count = {} # String -> Integer
    lowered_text = text.lower()

    for letter in lowered_text:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    return letter_count

def print_report(counted_letters_dict):
    characters = []

    for character in counted_letters_dict:
        if character.isalpha():
            characters.append({"character_name":character, "appearances": counted_letters_dict[character]})
    
    characters.sort(reverse = True, key = sort_on)
    
    for character in characters:
        print(f"The '{character['character_name']}' character was found {character['appearances']} times")

def sort_on(dict):
    return dict["appearances"]

main()