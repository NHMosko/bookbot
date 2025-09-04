def count_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_dict(in_dict):
    dict_list = []
    for k in in_dict:
        v = in_dict[k]
        dict_list.append({"char": k, "num": v})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list