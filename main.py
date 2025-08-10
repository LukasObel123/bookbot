from stats import get_word_count
from stats import get_char_dict
from stats import get_sorted_dictionary
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



filepath = sys.argv[1]
#filepath = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def make_report(book_text):
    num_words = get_word_count(book_text)
    char_dict = get_char_dict(book_text)
    sorted_list_dict = get_sorted_dictionary(char_dict)

    Title = "============ BOOKBOT ============"
    Analyze = f"Analyzing book found at {filepath}..."
    Word_count_title = "----------- Word Count ----------"
    Word_count = f"Found {num_words} total words"
    Char_count_title = "--------- Character Count -------"
    End_title = "============= END ==============="
    Char_count = ""
    for char in sorted_list_dict:
        line = f"{char["char"]}: {char["num"]} \n"
        Char_count +=  line


    Report_Text = "\n".join([Title,Analyze,Word_count_title,Word_count,Char_count_title,Char_count[:-1],End_title])
    return Report_Text

def main():
    book_text = get_book_text(filepath)
    

    print(make_report(book_text))

main()
