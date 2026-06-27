

#To store something
#   We use  variables   when  there  is only   one thing  to store

health =   90
name =  "Ali"

# When do we  use   an Array / List ?
#  -->  When we  have mutlply  values

#Example :  Name of your class fellows
class_fellows = ["Ali", "Ahmed", "Ayesha"]



#When to   use a  dictionary
# ->  When an object has some information about  it 

Movie = {
"Name":  "Kung Fu Panda",
"Year":  2010,
"Rating":  8.5,
"Characters": ["Po","Shifu","Tigress"]
}


#Whenever we   need to make  a   decision
#   we  use  if condition statement

marks = 80

if  marks >= 90:
    print("A+") 
elif marks >= 80:
    print("A")      
elif marks >= 70:
    print("B")      
elif marks >= 60:
    print("C")  
else:
    print("Fail")

# When we  need  to  repeat  an  action
#  ->  we  use  LOOPS
#  -> TYPES OF  LOOPS:
#   1. For Loop -> When we  already know how  many times  it  will repeat
#   2. While Loop -> Runs until a condition is met
'''  for loop example


     for i  in range(10):
            print(i)


 while  loop example

flag = False
i = 0

    while Flag == False:
        i = i   + 1
        if i  == 10:
            flag  = True

'''


# When we need to repeat certain  code later as  well
# ----->  Functions
#Defining the function
def greet(user):
    print(f"Hello there {user}")
    print(f"Welcome to our class")
    print(f"Hope you have a  great time") 

#calling the  function
greet("Ali")
greet("Krish")


# What  do we use if we need  to compare two numbers/variables
#---->  Comparision Operators
# if  age == 10         # equals  comparision
# if age != 5          #  not equals  to  comparision
#   >
#   <
#  >=
#  if age <=  9


#When we need more than one condition
# -----> Logical Operators  ( and,  or  ,  not)
age = 50
height = 300

if age  > 5 and  height > 100:
       print("You  are allowed  on the ride")
else:
        print("You are not allowed on the ride")


'''Write a condition  that  a person  should  be  allowed  a present if  the Maths_Marks are  atleast 70  and ( behavior  is good  or behavior is fine )
'''


math_marks = 80
behavior = "good"

if   math_marks >= 70 and (behavior == "good" or behavior == "fine"):
    print("Present  allowed")
else:
     print("Present not  allowed")


# what if we need to  find  something in an array
Names = ["Aarav","Eshaan","Aliyan","Krish","Josh","Kate"]


#checking if Kate   exists in the names  list


if "Kate" in  Names:
     print("Kate is present")



code =  "SIOAPDOAS923048I32-0virus2309490239SDFNSDFLKSDLKF"

if "virus" in code:
     print("VIRUS DETECTED. ANTIVIRUS ACTIVATED!")