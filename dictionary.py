#Dictionaries



contacts = {
    "Krish " : 8234923  ,
    "Eshaan" :  23948023 ,
    "Aarav" :  23804293 ,
    "Ali" : 283428934,
 }
  # Krish is the key and 8234923 is the value

'''Task: Make a dictionary. The keys should  be ur name , ur age and  your hobby.'''


my_info = {
    "name" : "aliyan", 
    "age" : 21 ,
    "hobby" : ["coding", "eating streetfood"]
}

print(my_info["hobby"])
print(my_info["hobby"][0])


#Task: Make a dictionary of your 5 friends. The keys should be their names and the values should be their ages.


fruits  = {
    "Apple" : "red",    
    "Banana" : "yellow",
    "Grapes" : "green",
    "Mango" : "yellow",
}

del fruits["Mango"]





ages = {
    "Krish" : 9 ,
    "Ali" : 21 ,
    "Aarav" : 10 ,
    "Eshaan" : 9
}

ages["Jimmy"] = 7
del ages["Jimmy"]


for key in ages:
    print(key)

