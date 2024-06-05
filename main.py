def main():
    frankenstein_path = "books/frankenstein.txt"
    book = get_book_text(frankenstein_path)
    word_count = count_book_words(book)
    character_count = get_character_count(book)
    print_report(frankenstein_path, word_count, character_count)
    return 0

def sort_on(dict):
    return dict["num"]

def print_report(book_path, word_count, character_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for character in character_count:
        if character["name"].isalpha():
            print(f"The {character['name']} character was found {character['num']} times")
    print("--- End report ---")

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def count_book_words(book):
    words = book.split()
    return len(words)

def get_character_count(book):
    character_list = []
    character_dict = {}
    for c in book:
        if c.lower() not in character_dict:
            character_dict.update({f"{c.lower()}": 1})
        else:
            character_dict[f"{c.lower()}"] += 1
    for key in character_dict:
        character_list.append({"name": f"{key}", "num": character_dict[key]})
    character_list.sort(reverse=True, key=sort_on)
    return character_list

if __name__ == '__main__':
    main()
