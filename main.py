def main():
    text_path = "books/frankenstein.txt"
    with open(text_path) as f:
        file_contents = f.read()
    print_report(text_path, file_contents)


def count_words(text):
    words = text.split()
    print(f"{len(words)} words found in the document")

def char_quantity(text):
    lowercase_text = text.lower()
    chars_count = {}
    for char in lowercase_text:
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1
    
    ordered_chars = order_by_quantity(chars_count)

    for item in ordered_chars:
        print(f"The '{item}' character was found {chars_count[item]} times")

def print_report(text_path, text_content):
    print(f"--- Begin report of {text_path} ---")
    count_words(text_content)
    print("")
    char_quantity(text_content)
    print('--- End report ---')


def order_by_quantity(char_dict):
    sorted_dict = sorted(char_dict, reverse=True, key=lambda item: char_dict[item])
    return sorted_dict

main()