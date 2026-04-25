# #H1 Write a function to calculate the sum of numbers from 1 to N.
# def sumCalculation(n):
#     sum=0
#     for num in range(1,n):
#         sum+=num
#     return sum
# n =int(input("Enter your number: "))
# print(sumCalculation(n))

# #H2 Write a function that returns the square of a number.
# import math
# def squareNum(n):
#     return math.sqrt(n)
# n =int(input("Enter your number: "))
# print(int(squareNum(n)))
# #H3 Write a function that checks whether a number is even/odd.
# def OddEven(n):
#     return n%2
# n = int(input("enter your number : "))
# if(OddEven(n)==0):
#     print("number is even")
# else:
#     print("number is odd ")

# #H4 Write a function that returns the larger number from two given numbers.

 

# def largestNum(a,b):
#     return max(a,b)

# a =int(input())
# b=int(input())
# print(largestNum(a,b))


# #H5  	Write a Python program to create a list of 10 integers. Then perform the following operations:
#   #Append an element to the list.
#   #Insert an element at a specific position.
#   #Remove an element from the list.
#   #Pop an element from a specific position.
  
  
# li = list((1,2,3,4,10,12))
# print(li)
# li.append(6)
# print(li)
# li.insert(4,5)
# print(li)
# li.remove(3)
# print(li)
# li.pop(li[-1])
# print(li)

# #H6 Write a program to find all unique elements in the list.
# li =list((1,2,3,2,3,4,5,10,10,11,12,12))
# my_set = set(li)
# print(my_set)

# #H7 Write a Python program to calculate the mean of a list of numbers.
 
# li =list((1,2,3,2,3,4,5,10,10,11,12,12))
# sum=0
# for num in li:
#     sum+=num
# n = len(li)
# print("this is means: ",sum/n)

#H8 Classify Numbers into Even and Odd Lists
li =list((1,2,3,2,3,4,5,10,10,11,12,12))
odd=[]
even =[]
for num in li:
    if(num%2==1):
        odd.append(num)
    else:
        even.append(num)
print("odd number in list: ",odd)
print("even number in list: ",even)
