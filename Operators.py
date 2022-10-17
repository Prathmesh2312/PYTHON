#Operators:- Operators are used to perform operations on variables and vlaues
#1)Unary operators:- they contains only one operand. These operators are basically used to provide sign to the operand...

#2)Binary Operators:- Binary operators are operators with two operands that are manipulated to get the result.

#A)Arithmetic Operators:- They perform basic arithmetic operations like addition,subtraction
                            #There are seven arithmetic operators: + Addtion
#                                                                  - Subtraction
#                                                                  * Multiplication
#                                                                  / Division
#                                                                  ** Exponent
#                                                                   % Modulus
#                                                                   // floor Division"""


#B) Assignment operatiors:- These operatiors are used to assign values to the variables
                            #The assienment operator is used to store the value on the rignt hand side of the expression on the left hand side variable in expression
                """Example:
                            1) =    Assign value from rignt side operands to the left side operands
                            2) +=   It add rignt operand to the left operand and assign the result to left operand
                            3) -=   It subract right operand from the left operand and assign result to the left operand
                            4) *=   It multiplies right operand with the left operand and assign the result to the left operand
                            5) /=   It divides left operand with right operand and assign the result the left operand
                            6) %=   It takes modulus using two operands and assign the result to the left operand
                            7) **=  Performs exponential calculation on operators and assign value to the left operand
                            8) //=  Performs exponential calculation on operators and assign value to the left operand"""

#C) Relational or Comparision Operators:- Used to compare values
#               """Example:
#                           1) ==   If the value of two operands are equal, then the condition becomes true
#                           2) !=   If the value of two operands are not equal, then the condition becomes true
#                           3) >    If the value of left operator is greater than right operand then condition becomes true.
#                           4) <    If the value of left operator is less than right operand then condition becomes true.
#                           5) >=   If the value of left operator is greater than or equal to right operand then condition becomes true.
#                           6) <=   If the value of left operator is less than or equal to right operand then condition becomes true.

#D) Logical Operators:- These operators performs logical AND,OR,NOT. these operations are used to check two or more conditions. The resultant of these operator is always Boolean value.
#               """Example:-
#                           1) AND  If the both operands are true then condition becomes true
#                           2) OR   If any of two operands are non-zero then condition becomes true.
#                           3) NOT  Used to reverse the logical state of its operand."""

#E) Bitwise Operators:- Bitwise operator acts on a bit and performs bit by bit operation. When we use bitwise operator on the operands, the operands are firstly converted to bits and then the operation is performed.
    #These operators are binary operators and unary operators that can be operated on two operands or one operand.

#               """Example:-
#                           1) &   This operator performs AND operation between operands. Operator copies a bit, to the result, if it exists in both operands
#                           2) |   This operator performs OR operation between operands. It copies a bit, if it exists in either operand.
#                           3) ^   This operator performs XOR operation between operands. It copies the bit, If it is set in one operand but not both.
#                           4) ~   It is unary operator and has the effect of flipping bits i.e. opposite the bits operand
#                           6) <<  The left operands value is moved left by the number of bits specified by the right operand.
#                           7) >>  The left operands value is moved right by the number of bits specified by the right operand."""

#F) Identity Operators:- This operator is used to compare two memory addresses of two objects.
#               """Example:-
#                           1) is:-     Returns true if the variables on either side of the operator point to the same object and false otherwise. Example:- if A=3,B=3 print(A is B)   then it return True
#                           2)is not:-  Return False, if the variables on either side of the operator point to the same object and true otherwise. Example:- if A=3,B=3 print(A is not B)   then it return false"""


#G) Membership Operators:- This operator in python is used to find the existence of particular element in the sequence and used only with sequence like string,tuple,list,dictionary etc.
#               """Example:-
#                           1) in     :-  True if value is found in list or in sequence, and false if item is not in the list or in sequence.
#                           2) not in :-  True if value is not found in the list or sequence, and false if item is not in the list or in sequence.. """
