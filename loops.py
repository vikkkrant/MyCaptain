list1= [] #empty list

number = int(input("Enter number of elements : ")) #number of elements of list
for i in range(0,number):
    elements = int(input("Enter element : ")) #entering the element

    list1.append(elements) #adds element inside the list
print(list1)

x = 0
positive = [] #empty list
for x in range(0,number): 
    if list1[x] >= 0: #finds positive element inside the list
        positive.append(list1[x]) #adds only positive element to the new empty list
print(positive)



