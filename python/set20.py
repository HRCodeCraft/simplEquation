# Add a list of elements to a set
def add_elements_to_set(my_set):
    input_str = input("Enter a comma-separated list of elements to add: ")
    input_list = input_str.split(",")
    my_set.update(input_list)
    print("Updated set:", my_set)

# Return a new set of identical items from two sets
def identical_items(set1, set2):
    common_set = set1.intersection(set2)
    print("Identical items:", common_set)

# Get Only unique items from two sets
def unique_items(set1, set2):
    unique_set = set1.symmetric_difference(set2)
    print("Unique items:", unique_set)

# Update the first set with items that don’t exist in the second set
def update_set(set1, set2):
    new_items = set2.difference(set1)
    set1.update(new_items)
    print("Updated set:", set1)

# Remove items from the set at once
def remove_items_from_set(my_set):
    input_str = input("Enter a comma-separated list of elements to remove: ")
    input_list = input_str.split(",")
    my_set.difference_update(input_list)
    print("Updated set:", my_set)

# Return a set of elements present in Set A or B, but not both
def exclusive_items(set1, set2):
    exclusive_set = set1.symmetric_difference(set2)
    print("Exclusive items:", exclusive_set)

# Check if two sets have any elements in common. If yes, display the common elements
def common_items(set1, set2):
    common_set = set1.intersection(set2)
    if len(common_set) == 0:
        print("No common items")
    else:
        print("Common items:", common_set)

# Update set1 by adding items from set2, except common items
def update_set_except_common(set1, set2):
    new_items = set2.difference(set1)
    common_items = set1.intersection(set2)
    set1.difference_update(common_items)
    set1.update(new_items)
    print("Updated set:", set1)

# Remove items from set1 that are not common to both set1 and set2
def remove_items_except_common(set1, set2):
    common_items = set1.intersection(set2)
    set1.difference_update(set1.difference(common_items))
    print("Updated set:", set1)

set1 = set(input("Enter elements of set1 separated by space: ").split())
set2 = set(input("Enter elements of set2 separated by space: ").split())

print(f"set1: {set1}")
print(f"set2: {set2}")

while True:
    print("Select an operation:")
    print("1. Add elements to set 1")
    print("2. Add elements to set 2")
    print("3. Get identical items from two sets")
    print("4. Get only unique items from two sets")
    print("5. Update set 1 with items that don't exist in set 2")
    print("6. Remove items from set 1 or set 2")
    print("7. Get exclusive items from two sets")
    print("8. Check for common items in two sets")
    print("9. Update set 1 by adding items from set 2, except common items")
    print("10. Remove items from set 1 that are not common to both set 1 and set 2")
    print("0. Exit")

    choice = input("enter choice:")

    if choice == "1":
        add_elements_to_set(set1)
    elif choice == "2":
        add_elements_to_set(set2)
    elif choice == "3":
        identical_items(set1, set2)
    elif choice == "4":
        unique_items(set1, set2)
    elif choice == "5":
        update_set(set1, set2)
    elif choice == "6":
        print("Select a set to remove items from:")
        print("1. Set 1")
        print("2. Set 2")
        remove_choice = input()
        if remove_choice == "1":
            remove_items_from_set(set1)
        elif remove_choice == "2":
            remove_items_from_set(set2)
        else:
            print("Invalid choice")
    elif choice == "7":
        exclusive_items(set1, set2)
    elif choice == "8":
        common_items(set1, set2)
    elif choice == "9":
        update_set_except_common(set1, set2)
    elif choice == "10":
        remove_items_except_common(set1, set2)
    elif choice == "0":
        break
    else:
        print("Invalid choice")

