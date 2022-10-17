#Condition Statements:- In Python, Condition Statements are used to determine if a specific condition is met by testing weather a condition is True or false.

#TYPES OF CONDITION STATEMENTS:-


#A) If statement: The if statement executes a statement if a condition is True...

#                           Syntax: if Condition:
#                                       Statement(S)

# Example:- 1)To find the absolute value of an input number.

x=int(input("Enter an integer number:"))
y=x
if (x<0):
    x = -x
print("Absolute value of",y,'=',x)



#2) To find number is even or odd

number=int(input("Enter any number:"))
if(number%2)==0:
    print(number,"is Even number")
else:
    print(number,"is Odd number")





#B) if else Statement:- This statemnent svaluates test expression and will execute the body of if only when the test condition is true. If condition is false, the body of else is executed.

#                   Syntax:- if condition:
#                               statement(s)
#                            else:
#                               statement(s)


#Example: 1) To check input year is leap year or not.

year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")




#C) if elif else statement:- The elif is a short form of else if. It allows us to check multiple conditions.
#                              As soon as one of the conditions the if is true, the statement associated with that if is executed, and the rest of the ladder is bypassed. If none of the condition is true, then final else statement is executed...

#                       Syntax:
#                                   if(condition 1):
#                                      Statements
#                                   elif(Condition 2);
#                                      Statements
#                                          .
#                                          .
#                                          .
#                                  elif(condition - n)
#                                       Statements
#                                  else:
#                                       Statements


#Example:-1) Program to check weather the largest number among the three numbers..

x=int(input("Enter the first Number:"))
y=int(input("Enter the second Number:"))
z=int(input("Enter the third Number:"))
if(x>y) and (x>z):
    l=x
elif(y>x) and (y>z):
    l=y
else:
    l=z
print("Largest number is:",l)







#D) Nested If statement: When we write one if statement inside another if statement then it is called a nested if statement.

#                       Syntax:- if condition 1:
#                                   if condition 2:
#                                       statement 1
#                                   else:
#                                       statement 2
#                                   else:
#                                       Statement 3

#Example:

num=float(input("Enter any number:"))
if num>=0:
    if num == 0:
        print("Zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")
