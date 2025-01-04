
def count_words(file_contents):
    words = file_contents.split()
    count = len(words)
    return count

def get_file_content(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_duplicates(file_contents):
    pass
    lower_file_contents = file_contents.lower()
    count_dict = {}
    for char in lower_file_contents:
        if char in count_dict:
            count_dict[char]+=1 
        else:
            count_dict[char] = 1
    return count_dict

def print_report(word_count, dict):
    char_list = [{'letter': letter, 'count': count} for letter, count in dict.items()]
    char_list.sort(reverse=True, key = lambda dict : dict['count'])
    print("--- Begin report of books/frankenstein.txt ---\n")
    print(f"{word_count} words found in the document\n\n")
    for char_dict in char_list:
        if  char_dict["letter"] == " " or char_dict["letter"] == "\n":
            continue
        else:
            print(f"\'{char_dict['letter']}\' charater was found {char_dict['count']} times")
    print("--- End report ---")

def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_file_content(path_to_file)
    count = count_words(file_contents)
    char_count_dict = count_duplicates(file_contents)
    print_report(count, char_count_dict)
    

main()
