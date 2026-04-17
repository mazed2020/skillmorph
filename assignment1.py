##write a program to perform the substruction multiplication and division

def substruction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
a = int(input("enter your first number: "))
b= int(input("enter your second number: "))
print("subtraction: " ,substruction(a,b))
print("multiplication: ", multiplication(a,b))
print(" division: " , division(a,b))

##Write a program to declare variables for id, name, batch, and hometown, and assign values, and finally print

id = " SM-ML-2026-B2-047"
name = "Md Mazedul Islam"
batch= "2nd"
hometown="Tangail"

print(id," ",name," ",batch,"",hometown)

## H3: Write a program to change values of an integer variable
value_int=123
print("first assign value : ",value_int)
value_int=230
print("change assign value: ",value_int)

## H4: Write a program to take two string numbers and convert them to integers using explicit type conversion.
str_num1=input("enter value 1: ")
str_num2=input("enter value 2: ")

print("string value print as it without converstion type",type(str_num1),str_num1,type(str_num2),str_num2)
print("convert type this two string: ",type(int(str_num1)),str_num1,type(int(str_num2)),str_num2)



## H5: Write a program to calculate and print the average of the three numbers. Round the result to two decimal places.
a =int(input("1st number: "))
b =int(input("2st number: "))
c =int(input("3st number: "))
print("{:.2f}".format((a+b+c)/3))



## H6: Create a simple calculator that performs basic arithmetic operations (addition, subtraction, multiplication, division) based on user input.
 
a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
opr = input("enter your operator: ")

if opr == "+":
    print(a + b)
elif opr == "-":
    print(a - b)
elif opr == "*":
    print(a * b)
elif opr == "/":
    print(a / b)
else:
    print("Invalid operator")

 

## H7: Write a program that asks the user to enter a single character and determines whether it is a vowel or a consonant.
ch = input("enter your character: ")
if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="y":
    print("  vowel ")
else:
    print("constant")


## H8: Create a program that converts temperatures between Fahrenheit and Celsius based on user input.
temperature = int(input("enter faahrenheit value: "))
print((temperature-32)*(5/9))


## H9: Write a program that asks the user to enter three numbers and determines which one is the largest.

a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
c = int(input("enter your 3rd number:  "))
if a>b and a>c:
    print("largest number: ",a)
elif b>a and b>c:
    print("largest number: ",b)
else:
    print("largest number: ",c)


# H10: Write a program that prompts the user to input a number N and prints all even numbers between 1 and N using a for loop.
n = int(input("enter the number: "))
for i in range(1,n):
    if n%2==0:
        print(i)
# H11: Write a program that prompts the user to input a number N and calculates the sum of all numbers from 1 to N that are divisible by 3 or 5.

n =int(input("enter the number"))

sum=0
for i in range(1,n):
    if(i%3 or i%5):
        sum+=i
print("summation of value that are divisible by 3,5: ",sum)


# H12: Write a program that prompts the user to input a number n and prints the multiplication table of n (1 to 10) using a for loop.

n = int(input())
mul=1
for i in range(1,n):
    mul*=i
print(mul)