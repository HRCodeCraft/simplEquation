import pandas as pd

def manipulate_series():
    data = []
    num_elements = int(input("Enter the number of elements in the series: "))

    for i in range(num_elements):
        element = int(input(f"Enter element {i+1}: "))
        data.append(element)

    series_data = pd.Series(data)
    print("\nSeries:")
    print(series_data)

    while True:
        print("\nSelect an operation:")
        print("1. Access a value")
        print("2. Modify a value")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            index = int(input("Enter the index to access: "))
            if 0 <= index < len(series_data):
                print("Value:", series_data[index])
            else:
                print("Invalid index!")
        elif choice == 2:
            index = int(input("Enter the index to modify: "))
            if 0 <= index < len(series_data):
                value = int(input("Enter the new value: "))
                series_data[index] = value
                print("Modified Series:")
                print(series_data)
            else:
                print("Invalid index!")
        elif choice == 3:
            break
        else:
            print("Invalid choice!")

def manipulate_dataframe():
    data = {}
    num_rows = int(input("Enter the number of rows in the DataFrame: "))
    num_columns = int(input("Enter the number of columns in the DataFrame: "))

    for i in range(num_columns):
        column_name = input(f"Enter the name of column {i+1}: ")
        column_data = []

        for j in range(num_rows):
            element = input(f"Enter value for column '{column_name}' and row {j+1}: ")
            column_data.append(element)

        data[column_name] = column_data

    df = pd.DataFrame(data)
    print("\nDataFrame:")
    print(df)

    while True:
        print("\nSelect an operation:")
        print("1. Access a column")
        print("2. Access a row")
        print("3. Modify a value")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            column_name = input("Enter the name of the column to access: ")
            if column_name in df.columns:
                print(df[column_name])
            else:
                print("Invalid column name!")
        elif choice == 2:
            index = int(input("Enter the index to access: "))
            if 0 <= index < len(df):
                print(df.iloc[index])
            else:
                print("Invalid index!")
        elif choice == 3:
            column_name = input("Enter the name of the column to modify: ")
            if column_name in df.columns:
                index = int(input("Enter the index to modify: "))
                if 0 <= index < len(df):
                    value = input("Enter the new value: ")
                    df.at[index, column_name] = value
                    print("Modified DataFrame:")
                    print(df)
                else:
                    print("Invalid index!")
            else:
                print("Invalid column name!")
        elif choice == 4:
            break
        else:
            print("Invalid choice!")

def main():
    print("1. Manipulate Series")
    print("2. Manipulate DataFrame")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        manipulate_series()
    elif choice == 2:
        manipulate_dataframe()
    else:
        print("Invalid choice!")

if __name__ == '__main__':
    main()
