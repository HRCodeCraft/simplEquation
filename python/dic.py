def demonstrate_dictionary_methods():
    my_dict = {}

    while True:
        print("\nDictionary:", my_dict)
        print("1. Add key-value pair")
        print("2. Access keys")
        print("3. Access values")
        print("4. Access items")
        print("5. Modify a value")
        print("6. Remove a key-value pair")
        print("7. Remove an arbitrary key-value pair")
        print("8. Clear dictionary")
        print("9. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter key: ")
            value = input("Enter value: ")
            my_dict[key] = value
            print("Key-value pair added.")

        elif choice == "2":
            print("Keys:", my_dict.keys())

        elif choice == "3":
            print("Values:", my_dict.values())

        elif choice == "4":
            print("Items:", my_dict.items())

        elif choice == "5":
            key = input("Enter key to modify value: ")
            if key in my_dict:
                value = input("Enter new value: ")
                my_dict[key] = value
                print("Value modified.")
            else:
                print("Key not found in the dictionary.")

        elif choice == "6":
            key = input("Enter key to remove: ")
            if key in my_dict:
                del my_dict[key]
                print("Key-value pair removed.")
            else:
                print("Key not found in the dictionary.")

        elif choice == "7":
            if my_dict:
                removed_key, removed_value = my_dict.popitem()
                print("Arbitrary key-value pair removed:", (removed_key, removed_value))
            else:
                print("Dictionary is empty.")

        elif choice == "8":
            my_dict.clear()
            print("Dictionary cleared.")

        elif choice == "9":
            break

        else:
            print("Invalid choice. Please try again.")


demonstrate_dictionary_methods()
