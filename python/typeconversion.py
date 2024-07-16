print("type conversions \npress 1 for int() conversion \n press 2 for float() conversions \n press 3 for str() conversion \n press 4 for chr() conversion \n press 5 for complex() conversion \n press 6 for ord() conversion  \n press 7 for hex() conversion \n press 8 for oct() conversion")
choice=int(input("enter your option: ")) 

if choice == 1:
        # Converting user input to an integer
        num_int = int(input("enter a number: "))

        # Using the int value to perform various type conversions
        num_float = float(num_int)
        num_str = str(num_int)
        num_hex = hex(num_int)
        num_oct = oct(num_int)
        num_chr = chr(num_int)
        num_ord = ord(num_chr)
        num_complex = complex(num_int)

        # Printing the results
        print("Integer: ", num_int)
        print("Float: ", num_float)
        print("String: ", num_str)
        print("Hexadecimal: ", num_hex)
        print("Octal: ", num_oct)
        print("Character: ", num_chr)
        print("ASCII value: ", num_ord)
        print("Complex number: ", num_complex)

elif choice == 2:
        # converting user input to an float
        user_input = float(input("Enter a number: "))

        # Using the float value to perform various type conversions
        num_int = int(user_input)
        num_str = str(user_input)
        num_chr = chr(int(user_input))
        num_complex = complex(user_input)
        num_ord = ord(chr(int(user_input)))
        num_hex = hex(int(user_input))
        num_oct = oct(int(user_input))

        # Printing the results
        print("Float: ", user_input)
        print("Integer: ", num_int)
        print("String: ", num_str)
        print("Character: ", num_chr)
        print("Complex number: ", num_complex)
        print("Unicode code point: ", num_ord)
        print("Hexadecimal: ", num_hex)
        print("Octal: ", num_oct)

elif choice == 3:
        # converting user input to string
        user_input = input("Enter a string: ")

        # Using the string value to perform various type conversions
        num_int = int(user_input)
        num_float = float(user_input)
        num_chr = chr(int(user_input))
        num_complex = complex(user_input)
        num_ord = ord(user_input[0])
        num_hex = hex(int(user_input))
        num_oct = oct(int(user_input))

        # Printing the results
        print("String: ", user_input)
        print("Integer: ", num_int)
        print("Float: ", num_float)
        print("Character: ", num_chr)
        print("Complex number: ", num_complex)
        print("Unicode code point: ", num_ord)
        print("Hexadecimal: ", num_hex)
        print("Octal: ", num_oct)

elif choice == 4:
        # User input
        user_input = input("Enter a character: ")

        # Using the character value to perform various type conversions
        num_ord = ord(user_input)
        num_int = int(num_ord)
        num_float = float(num_ord)
        num_str = str(user_input)
        num_complex = complex(num_ord)
        num_hex = hex(num_ord)
        num_oct = oct(num_ord)

        # Printing the results
        print("Character: ", user_input)
        print("Unicode code point: ", num_ord)
        print("Integer: ", num_int)
        print("Float: ", num_float)
        print("String: ", num_str)
        print("Complex number: ", num_complex)
        print("Hexadecimal: ", num_hex)
        print("Octal: ", num_oct)

elif choice == 5:
        # User input
        user_input = input("Enter a complex number (in the format x+yj): ")

        # Parsing the complex number and extracting its real and imaginary parts
        real_part = float(user_input.split("+")[0])
        imag_part = float(user_input.split("+")[1].replace("j", ""))

        # Creating a complex number using the real and imaginary parts
        num_complex = complex(real_part, imag_part)

        # Using the complex number to perform various type conversions
        num_int = int(num_complex.real)
        num_float = float(num_complex.real)
        num_str = str(num_complex)
        num_chr = chr(int(num_complex.real))
        num_ord = ord(num_chr)
        num_hex = hex(num_ord)
        num_oct = oct(num_ord)

        # Printing the results
        print("Complex number: ", num_complex)
        print("Integer: ", num_int)
        print("Float: ", num_float)
        print("String: ", num_str)
        print("Character: ", num_chr)
        print("Unicode code point: ", num_ord)
        print("Hexadecimal: ", num_hex)
        print("Octal: ", num_oct)

elif choice == 6:
        # Taking a character as input from the user
        char_input = input("Enter a single character: ")
    
        # Converting the character to its corresponding Unicode integer value using ord()
        unicode_val = ord(char_input)
    
        # Converting the Unicode integer value to int, float, str, chr, complex, hex, and oct types
        int_val = int(unicode_val)
        float_val = float(unicode_val)
        str_val = str(unicode_val)
        chr_val = chr(unicode_val)
        complex_val = complex(unicode_val)
        hex_val = hex(unicode_val)
        oct_val = oct(unicode_val)
    
        # Printing the converted values
        print("Integer value:", int_val)
        print("Float value:", float_val)
        print("String value:", str_val)   
        print("Character value:", chr_val)
        print("Complex value:", complex_val)
        print("Hexadecimal value:", hex_val)
        print("Octal value:", oct_val)

elif choice == 7:
        hex_num = input("Enter a hexadecimal number: ")
        print("integer",int(hex_num, 16))
        print("float",float.fromhex(hex_num))
        print("string",str(hex_num))
        print("character",chr(int(hex_num, 16)))
        hex_len = len(hex_num)
        if hex_len < 16:
         hex_num = '0'*(16-hex_len) + hex_num
        real = int(hex_num[:8], 16)
        imag = int(hex_num[8:], 16)
        print("complex",complex(real, imag))
        print("unicode code point",ord(chr(int(hex_num, 16))))

elif choice == 8:
        oct_num = input("Enter a number in octal format: ")
        dec_num = int(oct_num, 8)
        print("Decimal value:", dec_num)
        float_num = float(dec_num)
        print("Float value:", float_num)
        str_num = str(dec_num)
        print("String value:", str_num)
        chr_num = chr(dec_num)
        print("Character value:", chr_num)
        complex_num = complex(dec_num)
        print("Complex value:", complex_num)
        ord_num = ord(chr_num)
        print("Unicode value:", ord_num)
        hex_num = hex(dec_num)
        print("Hexadecimal value:", hex_num)