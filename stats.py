def get_num_words(text):
    words = text.split()
    return len(words)

def numbers_of_letters(text):
    char_counts = {}
    for letter in text.lower():
        if letter in char_counts:
            char_counts[letter] = char_counts[letter] + 1
        else:
            char_counts[letter] = 1
    return char_counts

def sort_on(item):
    return item["num"]

def build_sorted_letters(counts_dict):
    letters = []
    for ch, num in counts_dict.items():
        letters.append({"char": ch, "num": num})
    letters.sort(reverse=True, key=sort_on)
    return letters
