#### Question-1 ####

# num = input("Enter a number: ")

# if str(num) == str(num)[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#### Question-2 ####

# num=[2,3,4,5,6]

# avg=0
# for i in num:
#     avg += i
# avg =avg/len(num)
# print(f"Average of Numbers is : {avg}" )


#### Question-3 ####

# l1=[1,2,7]
# l2=[2,4,5]

# l=l1+l2
# print(f"List Before sorting : {l}")
# l.sort()
# print(f"List After sorting : {l}")


# take input from user
# list1 = list(map(int, input("Enter numbers for list1 (space separated): ").split()))
# list2 = list(map(int, input("Enter numbers for list2 (space separated): ").split()))

# # merge the lists
# result = list1 + list2

# # sort the result
# result.sort()

# print("Merged & Sorted List:", result)


#### Question-4 ####

# li=[2,3,4,5,6,7,8,9]
# even_li=[]
# odd_li=[]

# for i in li:
#     if i % 2 == 0 :
#         even_li.append(i)
#     else:
#         odd_li.append(i)

# print(even_li)
# print(odd_li)


#### Question-5 ####

# student={}
# while True:
#     print("\n---------- MENU ----------")
#     print("A - Add a student")
#     print("B - Update marks")
#     print("C - Search for a student")
#     print("D - Display all students and marks")
#     print("E - Exit")
#     print("--------------------------")

#     operation = input("Enter operation: ").upper()

#     # A → Add a student
#     if operation == 'A' :
#         name=input("Enter Name : ")
#         marks=int(input("Enter marks :"))
#         student[name]= marks
#         print("Student added succesffuly")
    
#     # B → Update marks
#     elif operation == 'B' :
#         name=input("Enter Name of student you want to update : ")
#         if name in student:
#             marks=int(input("Enter new marks :"))
#             student[name] = marks    
#             print("Marks updated")
#         else:
#             print("Student not found.")
    
#     # C → Search a student
#     elif operation == 'C':
#         name=input("Enter student name to search: ")
#         if name in student:
#             print(f"{name} → {student[name]} marks")

#         else:
#             print("Student not found.")

#     # D → Display all students
#     elif operation == 'D':
#         if len(student) == 0:
#             print("No students found.")
#         else:
#             print("\n--- Student List ---") 
            
#             for name, marks in student.items():
#                 print(f"{name} : {marks}")
    
#     # E → Exit
#     elif operation == 'E':
#         print("Exiting program... Goodbye!")
#         break

#     else:
#         print("Invalid choice! Try again.")


#### Question-6 ####

# words =["apple","banana","kiwi","cherry","mango"]

# words_dic={}

# for word in words:
#     words_dic[word]=len(word)
    
# print(words_dic)


#### Question-7 ####

# text= input("Enter string you want to enter: ")
# count_spaces=0

# for ch in text:
#     if ch==' ':
#         count_spaces+=1 

# print("Number of spaces:", count_spaces)

##### Alternate

# text = input("Enter a string: ")
# print("Number of spaces:", text.count(" "))


#### Question-8 ####

## list1 =[1,2,3,4] 
## list2 =[5,6,7,8]

# list1 =[1,2,3]
# list2 =[3,4]

# if set(list1).isdisjoint(set(list2)):
#     print("No common element")
# else:
#     print("Found Common element")


#### Question-9 ####

# lst = [1, 2, 3, 2, 4, 5, 3, 6, 3]

# seen=set()
# duplicate=set()

# for ele in lst:
#     if ele in seen:
#         duplicate.add(ele)
#     else :
#         seen.add(ele)

# print("Elements appearing more than once:", duplicate)


#### Question-10 ####

text=input("Enter String :")

unique_chars=set(text)

print("Unique characters:", unique_chars)
print("Count of unique characters:", len(unique_chars))
