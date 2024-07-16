tuple_1 = eval(input('Enter tuple 1: '))             #creating tuple 1
print(tuple_1)

tuple_2 = eval(input('Enter tuple 2: '))                 #creating tuple 2
print(tuple_2)


print("press 1 for conatenate\n press 2 for repeating\n press 3 for length\n press 4 for min and max \n press 5 for count \n press 6 for index \n press 7 for slice \n press 8 for delete \n press 9 for sum")
choice=int(input("enter your option: ")) 


if choice == 1:
        result = (tuple_1 + tuple_2)
        print("concatenate tuple : " , result)

elif choice == 2:
        a = int(input("how many time tuple 1 repeats: "))
        b = int(input("how many time tuple 2 repeats: "))
        print("repeating tuple 1 : ", tuple_1 * a)
        print("repeating tuple 2 : ", tuple_2 * b)

elif choice == 3:
        print("length of tuple 1: ", len(tuple_1))
        print("length of tuple 2: ", len(tuple_2))

elif choice == 4:
         print("minimum value of tuple 1: ", min(tuple_1))
         print("minimun value of tuple 2: ", min(tuple_2))
         print("maximum value of tuple 1: ", max(tuple_1))
         print("maximum value of tuple 2: ", max(tuple_2))

elif choice == 5:
        tuple1 = input("enter element to be counted: ")
        tuple2 = input("enter element to be counted: ")
        print("count of given element in tuple 1: ", tuple_1.count(tuple1))
        print("count of given element in tuple 2: ", tuple_2.count(tuple2))

elif choice == 6:
        tuple1 = input("enter element to know indexing from tuple 1: ")
        tuple2 = input("enter element to know indexing from tuple 2: ")
        print("element occured at index: ", tuple_1.index(tuple1))
        print("element occured at index: ", tuple_2.index(tuple2))

elif choice == 7:
        start_tuple1 = int(input("enter start index of tuple 1: "))
        end_tuple1 = int(input("enter end index of tuple 1: "))
        step_tuple1 = int(input("enter step size of tuple 1: "))
        start_tuple2 = int(input("enter start index of tuple 2: "))
        end_tuple2 = int(input("enter end index of tuple 2: "))
        step_tuple2 = int(input("enter step size of tuple 2: "))
        tuple1 = tuple_1[start_tuple1 : end_tuple1 : step_tuple1]
        tuple2 = tuple_2[start_tuple2 : end_tuple2 : step_tuple2]
        print("slice tuple 1: ", tuple1)
        print("slice tuple 2: ", tuple2)

elif choice == 8:
        del(tuple_1)
        del(tuple_2)
        print("tuple 1 after deleting: ", tuple_1)
        print("tuple 2 after deleting: " , tuple_2)

elif choice == 9:
        print("sum of tuple 1: ", sum(tuple_1))
        print("sum of tuple 2: ", sum(tuple_2))

else:
        print("invalid option")