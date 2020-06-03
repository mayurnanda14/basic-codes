"""
#=========================================================================
#Variables
#=========================================================================
1)Variables are memory locations where values are stored and it has a name
2)Variables are name value pair
3)value inside the variable can be accessed using its name
4)value can be stored in a variable using its name
5)variable name can contain letters,numbers and special characters like underscore
6)+ and - cannot be in variable name
7)variable name cannot start with a number
8)variable can have have upper case as well as lower case
9)variables are case sensitive

#========================================================================
#Strings
#========================================================================
1)Strings represent text
2)surrounded by quotes either double or single
3)if you want the quotes as string i.e you want to escape quote you can escape using backslash as shown in below example

""""
double="She said, \"That's a great tasting apple!\""
print(double)
single='She said ,"That\'s a great tasting apple!"'
print(single)


# each character in string has a index for eg.
fruit='apple'

#index of a is 0, p is 1, p is 2, l is 3, e is 4
#each character of string can be accessed using its index

first_character=fruit[0]

#in above example 'a' will be stored in variable first_character


"""
#==========================================================================
#Functions
#==========================================================================
1)function is section of reusable code that performs an action
2)A function has a name and is called or executed by that name
3)optionally a function can accept arguments and return data
4) python has many bult-in functions, one of it is print()
5) To print we can directly pass the value of through variables
"""
print(fruit)
# will print value stored in variable fruit
print('orange')
#will print string orange
print(len(fruit))
#will print length of value inside variable fruit
print(len('orange'))
#will directly print length of string 'orange'

"""
#=========================================================================
#Basic OOP
#=========================================================================
1)Everything in python is an object
2)Every object has a Type
3)'apple' is object of Type "str"------------>'apple' is a string object
4)fruit='apple'----------> fruit is a string object
5)object also has function but are not called functions but method
6)methods are functions that run against an object
7)TO call method on an object, format is as shown below
  object.method()
"""
print(fruit.upper())
#will print upper case of all characters of object inside fruit
print(fruit.lower())

#will print lower case of all characters of object inside fruit

#========================================================================
#string concatenation (adding two strings)
#========================================================================

print('I '+'love '+'Python')
#will add all the three strings and will give concatenated string 'I love Python'

first='I'
second='love'
third='Python'
sentence=first+' '+second+' '+third+'.'
print('sentence')

#=========================================================================
#Repeating string
#=========================================================================

print('-'*10)
#'-' is repeated 10 times (* is a repetation operator for string)
happines='happy'*3
#'happy' is repeated 3 times and stored in happiness

#==========================================================================
#str() function
#==========================================================================
version=3
print('I love Python '+str(version)+'.')

#==========================================================================
#formatting strings
#==========================================================================
print('I {} Python.'.format('love'))
print('{} {} {}'.format('I','love','Python'))
print('I {0} {1}. {1} {0}s me.'.format('love','Python'))
first='I'
second='love'
third='Python'
print('{} {} {}.'.format(first,second,third))
version=3
print('I love Python{}.'.format(version))
print('{0:8}|{1:8}'.format('Fruit','Quantity'))
print('{0:8}|{1:8}'.format('Apple',3))
print('{0:8}|{1:8}'.format('Oranges',10))
print('{0:8}|{1:<8}'.format('Fruit','Quantity')) #for left alignment of second character
print('{0:8}|{1:<8}'.format('Apple',3)) #for left alignment of second character
print('{0:8}|{1:<8}'.format('Oranges',10)) #for left alignment of second character
print('{0:8}|{1:<8.2f}'.format('Oranges',10.333333)) #for left alignment of second character and with 2 decimals


#============================================================================
#Getting user input
#============================================================================
fruit=input('Enter a name of fruit: ')
print('{} is lovely fruit'.format(fruit))

#============================================================================
#Arithmetic operations
#============================================================================
a=3
b=2
z='2'
c=a+b #will add value in variable 'a' with value in variable 'b' and store result in variable c.result will be of Type int as a and b are of type int
d=a*b #will multiply value in variable 'a' with value in variable 'b' and store result in variable c.result will be of Type int as a and b are of type int
e=a/b #will divide value in variable 'a' with value in variable 'b' and store result in variable c. result will be of Type float
f=3.333 #stores value 3.333 of type float in variable f
g=int(f) # converts value in variable of name f into int type and store in variable g
h=float(a) #converts value in variable of name a into float type and store in variable g
i=int(z) #converts string into integer
j=float(z) #converts string into float
#===========================================================================
#Boolean variable
#===========================================================================
y=True #Stores boolean value True in variable Y
z=False #Stores boolean value False in variable z

"""
Following operators give boolean values after operated on numerical values

== ------------- Equal to
>  ------------- Greater than
>= ------------- Greater than or equal to
<  ------------- Less than
<= ------------- less than or equal to
!= ------------- not equal to

"""
#==========================================================================
#Boolean operator
#==========================================================================
"""
Three following are Boolean operators
and
or
not
"""
#=========================================================================
#controlling order of operations
#=========================================================================
True and False or not False
True and False or True
True and False or True
False or True

#all above statement give result as True
# To control order of operation use parenthesis, anything surrounded by parenthesis is evaluated first and has its own unit

True and False or not False
(True and False) or (not False)
(True and False) or (not False)

#all above statements are same will give result as True

#============================================
#conditionals
#============================================
"""
if statement evaluates boolean expression inside it and then executes code block inside it
"""
if 37<40:
    print('Thirty seven is less than forty')
elif 37>40:
    print('Thirty seven is more than forty')
else:
    print('Thirt seven is equal to forty')

#==========================================================================
#Functions
#==========================================================================




#==========================================================================
#Lists
#==========================================================================
"""
1)list is a data type that holds an ordered collection of items
2)items can be of various data-types
3)you can even have lists in lists
4)Format of list is as follows
list_name=[item_1,item_2,item_N]
5)To create empty list-------------> list_name=[]
6)list_name[index]------->to accesss items in the list
"""
animals=['man','bear','pig']
#Each element of list has index , 'man' has index 0, 'bear' has index 1 and so on
animals[0] #To access man
animals[1] #To access bear
animals[2] #To access pig
#above indexing was from start, but from end we use negative numbers as shown below
animals[-1] #to access last element 'pig'
animals[-2] #to access second last element 'bear'
animals[-3] #to access third last element 'man'
#to add multiple elements in the list we use extend method
animals.extend(['cow','duck'])
more_animals=['horse','dog']
animals.extend(more_animals) #to add two lists
print(animals)
#to insert elements at particular index in the list use insert method
animals.insert(0,'horse') #'horse' will be inserted at 0 index and all other elements will be shifted right
print(animals)
animals.insert(2,'duck')
print(animals)
animals[0]='Tiger' #'Tiger' will replace element at 0 index
#to access portion of the listi.e slicing
#listname[index1:index2]------> starts from first index and goes upto index which is 1 less than index 2
#listname[:index2]------------> if first index is omitted 0 is assumed
#listname[index1:]------------> if second index is ommitted total number of items in the list is assumed
#listname[-2:0]---------------> will give last two elements, after colon total number of elements in the list is assumed
#we can consider strings as list of characters
animal='horse'
animal[1:4] #will give 'ors'
#exception-if we try to get the index of element which is not in the list
try:
    cat_index=animals.index('cat')
except:
    cat_index='no cats were found'
print(cat_index)

weekend_days=['Saturday','Sunday']
[sat,sun]=weekend_days #assign variables to each element of list
print(sat) #print content of variable sat
print(sun) #print content of variable sun
#======================================================================================================
#For loops-------->if you want to perform operation on every item in list use for loop
#======================================================================================================
animals=['man','bear','pig']
for animal in animals:
    up=animal.upper()
    print(up)

#======================================================================================================
#While Loop
#======================================================================================================
"""
while condition:
      Code block
"""
#accidently if we create infinite loop, then we can break out of loop by typing ctrl+c
animals=['man','bear','pig','cow','duck','horse']
index=0
while index<len(animals):
    print(animals[index].upper())
    index +=1

#======================================================================================================
#Sorting
#======================================================================================================
animals=['man','bear','pig']
sorted_animals=sorted(animals) #will sort alphabetically elements inside the list
more_animals=['lion','tiger','elephant']
allanimals=animals+more_animals
print(allanimals)

#======================================================================================================
#append
#======================================================================================================
animals=['man','bear','pig']
print(len(animals))
animals.append('cow')
print(len(animals))

#=======================================================================================================
#Ranges
#=======================================================================================================
#Range function gives list of numbers , mostly it is used with for statement to perform the operation for some fixed number of times,like accessing cantents of lists
for x in range(5):
    print(x)

for x in range(1,5): #to start at 1 and end at 4 in the interval of one
    print(x)

for x in range(1,10,2):  #will start at 1 and will increment in interval of 2 and will stop at value just before stop
    print(x)            #will print all odd values between 1 to 10

#to print all elements in the list
animals=['man', 'duck', 'bear', 'pig', 'cow', 'duck', 'horse', 'dog']
for x in range(len(animals)):
    print(animal[x].upper())
         #or#
for x in range(0,len(animals),1):
    print(animal[x].upper())
#==========================================================================================================
#Dictionaries[unordered collection of items]
#==========================================================================================================
"""
1)Dictionaries are datatypes that store key value pair called items
2)sometimes dictionaries are referred as associative arrays,hash tables and hashes
3)Dictionaries are created by comma separated items enclosed in curly braces
eg. dictionary_name={key_1:value1,---------,key_N:valueN}

4) to create empty dictionary---------> dict_name={}
5)items in key can be accessed by keys
"""
contacts={'Mayur':'9773672192','Manali':'9867697205'}
Mayur_mobile=contacts['Mayur'] #to give data for key Mayur
Manali_mobile=contacts['Manali'] #to give data for key Manali
print('Dial {0} to call Mayur \nDial {} to call manali'.format(Mayur_mobile,Manali_mobile))
contacts['Krishna']='9773736525'
print(contacts)
print(len(contacts))
del contacts['Krishna']
print(contacts)
print(len(contacts))
contacts={'Mayur':['9773672192','8369515552'],'Manali':'9867697205'}
for number in contacts['Mayur']:
    print(number)
#=========================================================================================================
#in operator used alog with if else and dictionary
#========================================================================================================= 
contacts={'Mayur':['9773672192','8369515552'],'Manali':'9867697205'}
if 'Mayur' in contacts.keys():
    print('Mayur\'s phone no: {}'.format(contacts['Mayur']))
if 'Mahesh' in contacts.keys():
    print('Mahesh\'s phone no: {}'.format(contacts['Mahesh']))

#==========================================================================================================
#Nested Dictionaries(data arranged in this way help us understand data better
#==========================================================================================================
contacts={'jason':{'phone':'555-0123','email':'jason@example.com'},'carl':{'phone':'555-0987','email':'carl@example.com'}}
for contact in contacts:
    print('{} contact info is :'.format(contact))
    print('phone no={}'.format(contacts[contact]['phone']))
    print('email id={}'.format(contacts[contact]['email']

#==========================================================================================================
#two variables in for loop for dictionaries
#==========================================================================================================
contacts={'Jason':'555-0123','carl':'555-0987'}
for person,phone_number in contacts.items():
    print('The number for {0} is {1}.'.format(person,phone_number))
          
#==========================================================================================================
#Tuples
#==========================================================================================================
"""
1) Tuple is an immutable list i.e contents cannot be changed(hence it is used when data is not to be changed while execution of the program)
2) Tuples are ordered
3) Values are accessed by index
4) we can perform many operations on tuple, that we used on Tuple like Iteration,Looping and concatenation
5) Everything on list is applicable on tuple but values inside tuple cannot be altered
6) To alter values Tuple can be changed to list
7)formar is as follows------------> tuple_name=(item1.item2,item3,.............,itemN)
8)format for tuple with one element----------> tuple_name=(item1,)
"""
days_of_week=('Monday','Tuesday','Wednesday','Thursday','Friday','saturday','Sunday')
monday=days_of_week[0]
print(monday)
for day in days_of_week: #To perform operation on every element of tuple use for loop
    print(day)
del days_of_week #we cannot change items of tuple but can completely remove tuple using del statement

days=list(days_of_week) #converts tuple to list
dayofweek=tuple(days) #convert list to tuple
type(dayofweek) #give class of object
weekend_days=('Saturday','Sunday')
(sat,sun)=weekend_days #assign variables to each element of tuple
print(sat) #print content of variable sat
print(sun) #print content of variable sun

#Tuple assignment to list
contactinfo=['9773672192','nanda.mayurkumar@gmail.com']
(phone,email)=contactinfo
print(phone)
print(email)                               
                               
#tuple assignment used in functions
def high_and_low(numbers):
    """Determine the highest and lowest number"""
    highest=max(numbers)
    lowest=min(numbers)
    return(highest,lowest)
lottery_numbers=[1,2,316,24,25,60]
(highest,lowest)=high_and_low(lottery_numbers)

#tuple inside list and values accessed using for loop
contacts=[('Mayur','9773672192'),('Manali','9867697205')]
for (name,phone) in contacts:
    print('{0}\'s phone no is {1}'.format(name,phone))


#=========================================================================================================
#Files
#=========================================================================================================

"""
1) To read input and to store output we require file)
2) Files are great to store data that remains if after execution of program
3) open() function opens a file and returns a file as object
4) 
"""




