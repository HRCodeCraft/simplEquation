from collections import Counter
import string

def most_frequent_words():
    file_name = input("enter the file name:")
    try:
        with open(file_name, 'r') as file:
            text = file.read().translate(str.maketrans("", "", string.punctuation))
            word_count = Counter(text.split())
            most_common = word_count.most_common(10)
            print("the 10 most frequent words in the file are: ")
            for word, count in most_common:
                print(word, ":", count)
    except FileNotFoundError:
        print("error: file not found")

most_frequent_words()
