def count_vowels(file_name):
    try:
        with open(file_name, 'r') as file:
            txt = file.read().lower()
            vowel_counts = {'a': 0, 'e':0, 'i':0, "o":0, 'u':0}
            for char in txt:
                if char in vowel_counts:
                    vowel_counts[char]+=1
            print("vowel count in the file: \n")
            for vowel,counts in vowel_counts.items():
                print(vowel+ ":" +str(counts))
    except FileNotFoundError:
        print("file not found")

file_name = input("enter the name of the file: ")
count_vowels(file_name)
