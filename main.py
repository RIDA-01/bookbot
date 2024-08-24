def count_characters(text):
    character_count = {}
    for char in text.lower():
        if char.isalpha():  # Count only alphabetic characters
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count

def count_words(text):
    words = text.split()  # Split the text into words using whitespace as a delimiter
    return len(words)  # Return the total number of words

def print_report(file_path, text):
    # Count characters and words
    character_count = count_characters(text)
    word_count = count_words(text)
    
    # Convert character_count dictionary to a list of dictionaries for sorting
    char_list = [{"char": char, "num": count} for char, count in character_count.items()]
    
    # Sort the list by the number of occurrences (in descending order)
    char_list.sort(reverse=True, key=lambda x: x["num"])
    
    # Print the report
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

def main():
    path_to_file = r'C:\Users\ridad\OneDrive\Desktop\visual studio\workspace\.gitignore\books\frankestein.txt'
    
    # Read the content of the file
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
    
    # Print the report
    print_report(path_to_file, file_contents)

# Call the main function
if __name__ == "__main__":
    main()
