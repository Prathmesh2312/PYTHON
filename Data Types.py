#standard data types in python
#1) Boolean:- It represents the two values True and False internally the True Value is represented as 1 and false is 0

#2)None Data type:- Python defines a special variable None denoting a NUll object

#3)Number data type
    #i) Integer(Int):- an int data type represents an integer number. an integer number is a number without any decimal or fractional point.
                    #Example:- A=10

    #ii) Floating points numbers:- A floating point number is a number that contains a decimal point....

    #iii) Complex Number:- A complex number is a number that is written in the form of a+bj
                        #Example:- x=a+4j

#4) String data type:- string is a collection of group of characters identified as a continous set of characters enclosed in a single cotes or double cotes
     #Example:-
str="Hello world"
print(str)
print(str[4])
print(str[0:4])     #String Slicing
print(len(str))
print(str[0:11])
print(str[0:10])
print(str[0:20])
print(str[0:11:2])          #For Skipping alternet element/Advance slicing

#functions of Strings
str1="My name is Prathmesh"
print(str1.isalnum())           #Alphanumeric string which has no spaces
print(str1.isalpha())
print(str1.endswith("Prathmesh"))
print(str1.count("m"))          #how many times specific alphabate present in the string
print(str1.capitalize())        #make first latter of the string captial
print(str1.find("is"))          #for searching specific character in the sring
print(str1.lower())             #For lower case
print(str1.upper())             #make all string capital/uppercase
print(str1.replace("name","tiger"))
                                    #Functions
#capitalize()	Converts the first character to upper case
#center()	Returns a centered string
#count()	Returns the number of times a specified value occurs in a string
#encode()	Returns an encoded version of the string
#endswith()	Returns true if the string ends with the specified value
#expandtabs()	Sets the tab size of the string
#find()	Searches the string for a specified value and returns the position of where it was found
#format()	Formats specified values in a string
#format_map()	Formats specified values in a string
#index()	Searches the string for a specified value and returns the position of where it was found
#isalnum()	Returns True if all characters in the string are alphanumeric
#isalpha()	Returns True if all characters in the string are in the alphabet
#isascii()	Returns True if all characters in the string are ascii characters
#isdigit()	Returns True if all characters in the string are digits
#isidentifier()	Returns True if the string is an identifier
#islower()	Returns True if all characters in the string are lower case
#isnumeric()	Returns True if all characters in the string are numeric
#isprintable()	Returns True if all characters in the string are printable
#isspace()	Returns True if all characters in the string are whitespaces
#istitle()	Returns True if the string follows the rules of a title
#isupper()	Returns True if all characters in the string are upper case
#join()	Converts the elements of an iterable into a string
#ljust()	Returns a left justified version of the string
#lower()	Converts a string into lower case
#lstrip()	Returns a left trim version of the string
#maketrans()	Returns a translation table to be used in translations
#partition()	Returns a tuple where the string is parted into three parts
#replace()	Returns a string where a specified value is replaced with a specified value
#rfind()	Searches the string for a specified value and returns the last position of where it was found
#rindex()	Searches the string for a specified value and returns the last position of where it was found
#rjust()	Returns a right justified version of the string
#rpartition()	Returns a tuple where the string is parted into three parts
#rsplit()	Splits the string at the specified separator, and returns a list
#rstrip()	Returns a right trim version of the string
#split()	Splits the string at the specified separator, and returns a list
#splitlines()	Splits the string at line breaks and returns a list
#startswith()	Returns true if the string starts with the specified value
#strip()	Returns a trimmed version of the string
#swapcase()	Swaps cases, lower case becomes upper case and vice versa
#title()	Converts the first character of each word to upper case
#translate()	Returns a translated string
#upper()	Converts a string into upper case
#zfill()	Fills the string with a specified number of 0 values at the beginning




#5) List data types:- List can contain homogenous values such as integer,float,strings,tuples,list and dictionaries but they are commonly used to store collection of homogenous objects..
        #in the list items can seprated by commas(,) are enclised within square brackets[]..
                    #Example:- first=[10,20,30,80]
list1=["ABC","123","XYZ","678"]
print(list1)
print(list1[3])
list1.append(456)       #Add any element in the last of the list
print(list1)
list1.insert(3,65)          #Add element in the list   format= (Index , Number or data
print(list1)
list1.remove(123)
print(list1)
                    #List Functions
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list

#6)Touple data types:- Touple is an ordered sequence of items same as list. The only difference is that touple once created cannot be modified...
                        # It is defined within parantheses() and seprated by commas(,)..
                        #Example:- touple_obj=(40,1.5,"Hello")

                        #Functions in Touple
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found


#7) Dictionary Data types:- it is a unordered collection of key-value pair
                            # items in the dictionaries are enclised in the curly braces{} and seprated by the comma(,). a colon(:) is used to seprate key from value
                            #Example:- dic1:-{1:"First","Second":2}
            #Functions in Dictionary
#clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a dictionary with the specified keys and value
#get()	Returns the value of the specified key
#items()	Returns a list containing a tuple for each key value pair
#keys()	Returns a list containing the dictionary's keys
#pop()	Removes the element with the specified key
#popitem()	Removes the last inserted key-value pair
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key-value pairs
#values()	Returns a list of all the values in the dictionary....
