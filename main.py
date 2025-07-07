from stats import get_num_words, get_char_count, sorted_char_count
import sys

def get_book_text(book_path):
    with open(book_path, 'r') as f:
        book_text = f.read()
        return book_text


def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        book_text = get_book_text(book_path)
        word_count = get_num_words(book_text)
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        char_count = get_char_count(book_text)
        sorted_count = sorted_char_count(char_count)
        for key,value in sorted_char_count(char_count):
            print(f"{key}: {value}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


if __name__ == '__main__':
    main()