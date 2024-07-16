list_1 = list(input("enter list1 elements: "))         #creating a list 1
print(list_1)

list_2 = list(input("enter list2 elements: "))         #creating a list 2
print(list_2)

print("press 1 for append\n press 2 for concatenate list\n press 3 for repeating the list\n press 4 for extend\n press 5 for insert\n press 6 for remove\n press 7 for pop\n press 8 for reverse\n press 9 for length\n press 10 for min and max\n press 11 for count\n press 12 for sort\n press 13 for index\n press 14 for slicing\n press 15 for deleting\n press 16 for clear")
choice=int(input("enter your option: ")) 

if choice == 1:
        list1 = input("enter element to append in list1 : ")
        list2 = input("enter element to append in list2 : ")
        list_1.append(list1)
        list_2.append(list2)
        print("append list_1 : ", list_1)
        print("append list_2 : ", list_2)

elif choice == 2:
        result = (list_1 + list_2)
        print("concatenate list : " , result)

elif choice == 3:
        a = int(input("how many time list1 repeats: "))
        b = int(input("how many time list2 repeats: "))
        print("repeating list 1 : ", list_1 * a)
        print("repeating list 2 : ", list_2 * b)

elif choice==4:
        list1 = input("enter element to extend: ")
        list2 = input("enter element to extend: ")
        list_1.extend(list1)
        list_2.extend(list2)
        print("extend list 1: ",list_1)
        print("extend list 2: ",list_2)

elif choice ==5:
        insertlist1 = input("enter element to be insert in list 1: ")
        indexlist1 = int(input("enter index at which the item to be inserted: "))
        insertlist2 = input("enter element to be insert in list 2: ")
        indexlist2 = int(input("enter index at which the item to be inserted: "))
        list_1.insert(indexlist1 , insertlist1)
        list_2.insert(indexlist2 , insertlist2)
        print("inserting elements in list 1 : ", list_1)
        print("inserting elements in list 2 : ", list_2)

elif choice ==6:
        list1 = input("enter element to remove from list 1: ")
        list2 = input("enter element to remove from list 2: ")
        list_1.remove(list1)
        list_2.remove(list2)
        print("remove element from list 1: ", list_1)
        print("remove elements from list 2: ", list_2)

elif choice ==7:
         indexlist1 = int(input("enter index at which the item to be pop: "))
         indexlist2 = int(input("enter index at which the item to be pop: "))
         list_1.pop(indexlist1)
         list_2.pop(indexlist2)
         print("popping elements in list 1 : ", list_1)
         print("popping elements in list 2 : ", list_2)

elif choice == 8:
        list_1.reverse()
        list_2.reverse()
        print("reverse list 1: ", list_1)
        print("reverse list 2: ", list_2)

elif choice == 9:
        print("length of list 1: ", len(list_1))
        print("length of list 2: ", len(list_2))

elif choice == 10:
         print("minimum value of list 1: ", min(list_1))
         print("maximum value of list 2: ", min(list_2))
         print("minimum value of list 1: ", max(list_1))
         print("maximum value of list 2: ", max(list_2))

elif choice == 11:
        list1 = input("enter element to be counted: ")
        list2 = input("enter element to be counted: ")
        print("count of given element in list 1: ", list_1.count(list1))
        print("count of given element in list 2: ", list_2.count(list2))

elif choice == 12:
         list_1.sort()
         list_2.sort()
         print("sort list 1: ", list_1)
         print("sort list 2: ", list_2)

elif choice == 13:
        list1 = input("enter element to know indexing from list 1: ")
        list2 = input("enter element to know indexing from list 2: ")
        print("element occured at index: ", list_1.index(list1))
        print("element occured at index: ", list_2.index(list2))

elif choice == 14:
        start_list1 = int(input("enter start index of list 1: "))
        end_list1 = int(input("enter end index of list 1: "))
        step_list1 = int(input("enter step size of list 1: "))
        start_list2 = int(input("enter start index of list 2: "))
        end_list2 = int(input("enter end index of list 2: "))
        step_list2 = int(input("enter step size of list 2: "))
        list1 = list_1[start_list1 : end_list1 : step_list1]
        list2 = list_2[start_list2 : end_list2 : step_list2]
        print("slice list 1: ", list1)
        print("slice list 2: ", list2)

elif choice == 15:
        start_list1 = int(input("enter start index of list 1: "))
        end_list1 = int(input("enter end index of list 1: "))
        step_list1 = int(input("enter step size of list 1: "))
        start_list2 = int(input("enter start index of list 2: "))
        end_list2 = int(input("enter end index of list 2: "))
        step_list2 = int(input("enter step size of list 2: "))
        del list_1[start_list1 : end_list1 : step_list1]
        del list_2[start_list2 : end_list2 : step_list2]
        print("deleting elements from list 1: ", list_1)
        print("deleting elements from list 1: ", list_2)

elif choice == 16:
        list_1.clear()
        list_2.clear()
        print("list 1 after clearing: ", list_1)
        print("list 2 after clearing: " , list_2)

else:
        print("invalid option")