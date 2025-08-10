def get_word_count(book_text):
    words_list = book_text.split()
    return len(words_list)

def get_char_dict(book_text):
    char_dict  = {}
    for char in book_text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def get_sorted_dictionary(char_dict):
    def sort_on(items):
        return items["num"]
    
    list_of_dicts = []
    for key in char_dict:
        if key.isalpha():
            character_dict = {"char": key,"num":char_dict[key]}
            list_of_dicts.append(character_dict)
    
    list_of_dicts.sort(key=sort_on)
    return list_of_dicts
    