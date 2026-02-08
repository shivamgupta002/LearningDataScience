##### Q1 ##### 

# salary=int(input("Enter your Salary:"))

# tax =lambda salary,rate:(salary* rate)/100

# if salary<30000:
#     salary -= tax(salary,5)

# elif salary>30000 and salary<70000:
#     salary -= tax(salary,15)

# elif salary>70000:
#     salary-=tax(salary,25)

# print(salary)


##### Q2 ##### 

# num1 = int(input("Enter 1st number :"))
# num2 = int(input("Enter 2nd number :"))

# print(f"Printing all Even numbers between {num1} and {num2} :")

# for i in range(num1,num2+1) : 
#     if i%2==0:
#         print(i)


##### Q3 ##### 

# a = int(input("Enter number :"))

# while (a > 0):
#     num=a%10
#     print(num)
#     a=a//10


##### Q4 ##### 

# a = int(input("Enter number :"))
# count=0
# while (a > 0):
#     num=a%10
#     count+=1
#     a=a//10

# print(count)


# ##### Q5 ##### 

# a = int(input("Enter number :"))

# sum=0
# while (a > 0):
#     num=a%10
#     sum+=num
#     a=a//10

# print(sum)


##### Q6 ##### 

# for i in range(1,101) :
#     if i%3==0 and i%5==0:
#         print(i)


##### Q7 ##### 

# while True:
#     num =input("Enter number : ")
#     if num == "Quit":
#         print("Quiting from program")
#         break

#     elif int(num) >0:
#         print("Poistive Number")

#     elif int(num) <0:
#         print("Negative Number")


##### Q8 ##### 

# def calclator (a,b,opertion):
#     if opertion=='+':
#         return a + b
#     elif opertion=='-':
#         return a - b
#     elif opertion=='*':
#         return a * b
#     elif opertion=='/':
#         return a / b
#     else:
#         return "Invalid operator"


# a = int(input("Enter 1st number :"))
# b = int(input("Enter 2nd number :"))
# operation = input("Enter operator :")
# result=calclator(a,b,operation)
# print(result)



##### Q9 ##### 

# def isPrime (n):
#     for i in range(2,n-1):
#         if n%i==0:
#             return "Not Prime"
#     return "Prime Number"

# n = int(input("Enter number :"))

# res=isPrime(n)
# print(res)


##### Q10 ##### 

while True:

    myNumber=13
    num=int (input("Enter your number :"))

    if num > myNumber:
        print("Too high")
    elif num< myNumber :
        print("Too Low")
    else:
        print("You Won")
        break

