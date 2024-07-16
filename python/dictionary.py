
n = int(input("enter no of inputs in dictionary 1: "))                              #creating dictionary 1

d1 = dict(input("Enter key and value: ").split() for _ in range(n))

print(d1)

n = int(input("enter no of inputs in dictionary 2: "))                              #creating dictionary 2

d2 = dict(input("Enter key and value: ").split() for _ in range(n))

print(d2)

print("press 1 for delete\n press 2 for update\n press 3 for length \n press 4 for keys in dictionary \n press 5 for vales in dictionary  \n press 6 for items in dictionary \n press 7 for get value \n press 8 for set_default\n press 9 for pop \n press 10 for form_key \npress 11 for clear ")
choice=int(input("enter your option: ")) 

if choice == 1:
        key1= input("which key1 wants to delete: ")
        key2= input("which key2 wants to delete: ")
        del d1[key1]
        del d2[key2]
        print("deleting elements from list 1: ", d1)
        print("deleting elements from list 1: ", d2)

elif choice == 2:
        d1.update(d2)
        print("update dictionary 1: ", d1)
        d2.update(d1)
        print("update dictionary 2: ", d2)

elif choice == 3:
        print("length of dictionary 1: ", len(d1))
        print("length of dictionary 2: ", len(d2))

elif choice == 4:
        print("keys in dictionary 1:",d1.keys())
        print("keys in dictionary 2:",d2.keys())

elif choice == 5 :
        print("values in dictionary 1:",d1.values())
        print("values in dictionary 2:",d2.values())

elif choice == 6:
        print("items in dictionary 1:",d1.items())
        print("items in dictionary 2:" ,d2.items())

elif choice == 7:
        key1 = input('enter key to get the value from dictionary 1: ')
        print("get value from dictionary 1:",d1.get(key1))
        key2 = input('enter key to get the value from dictionary 2: ')
        print("get the value from dictionary 2:",d2.get(key2))

elif choice == 8:
        key1 = input('enter key dictionary 1: ')
        value1 = input('enter value dictionary 1: ')
        print("set default key:value from dic_1:",d1.setdefault(key1,value1))
        key2 = input('enter key dictionary 2: ')
        value2 = input('enter value dictionary 2: ')
        print("set default key:value from dic_2: ",d2.setdefault(key2,value2))
        

elif choice == 9:
        key1 = input('enter key to get pop from dictionary 1: ')
        d1.pop(key1)
        print("after popping dictionary 1:", d1)
        key2 = input('enter key to get pop from dictionary 2: ')
        d2.pop(key2)
        print("after popping dictionary 2:", d2)

elif choice == 10:
        n = int(input("enter no. of keys:"))
        x = tuple(input("enter keys1 name:"))
        y = input("enter values1 name: ")
        d3 = dict.fromkeys(x, y)
        print("form_key of new dic3:",d3)

        i = int(input("enter no. of keys:"))
        a = tuple(input("enter keys1 name:"))
        b = input("enter values1 name: ")
        d4 = dict.fromkeys(a, b)
        print("form_key of new dic4:",d4)

elif choice == 11:
        d1.clear()
        print("clearing dictionary 1:", d1)
        d2.clear()
        print("clearing dictionary 2: ", d2)

else:
        print("invalid option")
        


