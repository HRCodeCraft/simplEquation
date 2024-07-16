import language_tool_python

def syntax_check(sentence):
    tool = language_tool_python.LanguageTool('en-US')

    # Check for errors in the sentence
    matches = tool.check(sentence)

    if len(matches) == 0:
        print("No grammatical errors found!")
    else:
        print("Grammatical errors found:")
        for error in matches:
            print("Error:", error.ruleId, "-", error.message)
            print("Suggested Correction:", error.replacements)
            print("")

def main():
    print("Welcome to the English Grammar Syntax Checker!")
    print("Please enter a sentence to check its syntax (type 'exit' to quit).")

    while True:
        sentence = input("Enter a sentence: ")
        if sentence.lower() == 'exit':
            print("Exiting program.")
            break
        else:
            syntax_check(sentence)

if __name__ == "__main__":
    main()
