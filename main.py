from stats import get_num_words, get_char_count,sortList
import sys
def get_book_text(path):
    with open(path) as f :
        file_contents = f.read()
    return file_contents

def printReport(list,count):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for item in list:
        print(f"{item["word"]} : {item["count"]}" )

def main():
    path = sys.argv[1]
   
    file_contents = get_book_text(path)
    count = get_num_words(file_contents)
    counts = get_char_count(file_contents)
    sortedList = sortList(counts)
    printReport(sortedList,count)
    

main()