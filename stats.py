
def get_num_words(text):
    split_book_text = text.split()
    return len(split_book_text)

def get_char_count(text):
    char_dict = {}

    for char in text:
        char = char.lower()
        if char.isalpha():
            try:
                char_dict[char] = char_dict[char] + 1
            except KeyError:
                char_dict[char] = 1
    return char_dict

def sorted_char_count(char_dict):
    return sorted(char_dict.items(), key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    with open('./books/frankenstein.txt', 'r') as f:
        text = f.read()
        print(get_char_count(text))

        char_dict = get_char_count(text)
        print(sorted_char_count(char_dict))
        for key, value in sorted_char_count(char_dict):
            print(f"{key}: {value}")
