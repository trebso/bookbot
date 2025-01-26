def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    counts = {}
    for letter in text:
        lower_case = letter.lower()
        if lower_case.isalpha():
            if lower_case not in counts:
                counts[lower_case] = 1
            else:
                counts[lower_case] += 1
    return counts

# Main program
with open("books/frankenstein.txt") as f:
    text = f.read()
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document\n")
    
    # Convert and sort the characters
    char_list = []
    counts = count_chars(text)
    for char in counts:
        char_list.append({"char": char, "count": counts[char]})
    
    char_list.sort(key=lambda x: x["count"], reverse=True)
    
    # Print each character count
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    
    print("--- End report ---")
