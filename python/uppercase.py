def convert_file_to_lower_upper_case(file_name):
    try:
        # Read the file
        with open(file_name, 'r') as file:
            file_content = file.read()

        # Convert to lowercase
        lower_case_content = file_content.lower()

        # Convert to uppercase
        upper_case_content = file_content.upper()

        # Write the lowercase content to a new file
        with open('lowercase_' + file_name, 'w') as file:
            file.write(lower_case_content)

        # Write the uppercase content to a new file
        with open('uppercase_' + file_name, 'w') as file:
            file.write(upper_case_content)

        print("Conversion successful. Check the files: 'lowercase_" + file_name + "' and 'uppercase_" + file_name + "'.")

    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("An error occurred while reading/writing the file.")

# Test the function
file_name = input("Enter the file name: ")
convert_file_to_lower_upper_case(file_name)