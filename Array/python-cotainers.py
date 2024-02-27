print("hello")
# ____________________________________________________________________________________________________________________________________
                                                            # DICTIONARIES
# ____________________________________________________________________________________________________________________________________

 # Python’s dictionary, list and tuple are the most common data types used as containers for collections of data.
student={
    "name": "Ellie",
    "course": "SEI",
    "age": 32
}
print(len(student))
option = 3

d = {
  option: 'three'
}

# WAYS TO RETRIEVE INFO FROM DICTIONARY:

#1- Bracket Notation to retrieve
student["status"] = "single"
print(student)

#2- Get method to retrieve -> provide default value to avoid KeyError
print(student.get("name"))
print(student.get("status"))
print(student.get("skills"))
student["skills"] = {"html":5, "css":4}
print(student.get("skills"))
print(student.get("soft_skills"))
# Provide a default value if key not in dictionary
print(student.get("soft_skills", {"communication"}))

#3- in operator
if "course" in student: 
    print (True)
    print(f'{student["name"]} took {student["course"]}')

# Deleting Keys and Values (ite: Property)
del student["age"]
print ("age" in student)


#Count
print(student)
print(len(student))



#Iteration

# for...in loops are used to iterate over the items in a dictionary.
# The preferred approach is to use the items() method to obtain a dictionary view object.
# student.items() returns a wrapped list of (key, value) tuples:

for key in student:
    print(f'{key}= {student[key]}')

# The preferred approach -> 1- returns a list of tuples
print(student.items())
# 2- now for loop to destructure the tuples
for key,val in student.items():
    print(f'{key}={val}')

# give tuples -> immutable -> not good enough
for item in student.items():
    print(item)

# Dictionary Practice Exercise 
'''Define a Python dictionary named where_my_things_are containing a few items where:
the keys are things you have, and
the values are the locations you keep those things.
Write a for...in loop that iterates over the items in the dictionary and prints each one as
My [thing] is kept [location]'''

where_my_things_are ={
    "clothes": "closet",
    "car": "parking",
    "silverware": "kitchen",
    "towel": "restroom"
}
# 1 - .items() -> to give a list of tuples
# 2 - tuples destructutre with foor loop

print(where_my_things_are.items())
for key,val in where_my_things_are.items():
    print(f'my {key} is kept at my {val}')


# ____________________________________________________________________________________________________________________________________
                                                            # LIST
# ____________________________________________________________________________________________________________________________________
# Python’s dictionary, list and tuple are the most common data types used as containers for collections of data.
# Lists can contain items of different types, including dictionaries and nested lists.
# Lists are considered to be a sequence type in Python. 
# A sequence is a generic term used for an ORDERED collection. Other sequence types in Python include strings and tuples.
colors = ["blue", "red", "green"]
print(len(colors))
colors[0] = "black"
colors[-1] = "pink"
print(colors)


# Add Items

# APPEND METHOD
colors.append("green")
print(colors)
# unlike JS’s push() method, append() can only add one item and does not return a value.
# EXTEND METHOD
colors.extend(["brown", "gray"])
print(colors)
# CONCATINATION METHOD
colors+=["navy", "maroon"]
print(colors)
odds = [1, 3, 5]
evens = [2, 4, 6]
print(odds+evens)


# Insertig Itmes
colors.insert(2, "sage")
print(colors)



# Removing Items -> specify the index to be removed

# Pop
colors.pop()
print(colors)
colors.pop(2)
print(colors)


# Deleting ->If you don’t care about the value returned by pop(), you can also use the del operator to delete an item:
del colors[5]
print(colors)


# Remove
colors.remove("black")
print(colors)

# Clearing an Entire List -> .clear() method
# colors.clear()
print(colors)

# Iterating Over Items in a List
for color in colors:
    print (color)

    # or

for idx, color in enumerate(colors):
    print(f"at {idx} position the color is {color}")


# Lists & Dictionary Practice Exercise 
#  
#  Define a list named scores that contains a dictionary with the following shape:
#  scores = [
#    {
#      'name': 'name of the player',
#      'points': 25  # points the player scored
#    }
#  ]
# Next, using append(), to add an additional “score” dictionary to the scores list.
# Iterate over the items in the scores list and print a string with this format
#  <name> scored <points> points
# for each dictionary item in the list.  

scores = [{
    "name": "ellie",
    "points": 25
}]
scores.append({"name": "amir", "points": 30})
print(scores)
scores.extend([{"name": "abbas", "points": 24}, {"name": "pouya", "points":69}])
print(scores[0]["name"])
# scores.forEach((score)=>{
#     print(score["name"])

# })
for score in scores:
    print(f"{score['name']} scored {score['points']} points")


# *********************** #
#  LIST COMPREHENSION -> nice way to MAP a list -> [<to do expression> for items in <array name>]
# *********************** #
    # non-comprehension approach -> using a for...in loop
    
# List comprehensions provide a concise way to create lists
    
# WAY 1 OF LIST CREATION/COMPREHENSION
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
print(x) #9

# WAY 2 OF LIST CREATION/COMPREHENSION -> NO SIDE EFFECT
# Note that this creates (or overwrites) a variable named x that still exists after the loop completes.
# We can calculate the list of squares without any side effects using:    
square_a = [x**2 for x in range(10)]
print("squares_a",square_a)
# print(x)
# NameError: name 'x' is not defined

# WAY 3 OF LIST CREATION/COMPREHENSION -> NO SIDE EFFECT
square_b = list(map(lambda x:x**2,range(16)))
print("squares_b",square_b)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_c = [n**2 for n in nums]
print("squares_c", squares_c)
squares_d=list(map(lambda n: n**2, nums))
print("squares_d",squares_d)


# Here’s the basic syntax of a list comprehension:
# [<expression> for <item> in <list>]
# This reads as: I want <do expression> for each <item> in <list> -> a modified for...in loop within square brackets that returns a new list.
a= [n for n in nums]
# iteration in list in python
print(a)


#  LIST COMPREHENSION -> nice way to MAP a list -> [<to do expression> for items in <array name>]

#  LIST FILTERING ->[<to do expression> for items in <array name> if this condition is met]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_even = [n**2 for n in nums if(n%2==0)]
print(square_even)
# ____________________________________________________________________________________________________________________________________
                                                            # TUPLES
# ____________________________________________________________________________________________________________________________________
# Python’s dictionary, list and tuple are the most common data types used as containers for collections of data.   
# Tuples in Python are very similar to Python lists. -> but they are immutable
# Since tuples can’t be changed after they are created, they are great for protecting data that you don’t want to be changed.
# Tuples internally are “lighter weight” than lists and Python iterates over tuples faster than lists.
# Because they are immutable, tuples can even be used as keys for dictionaries.
# Generally, you’ll find that tuples are used to contain heterogeneous (different) data types and lists for homogeneous (similar) data types.

# You may come across tuple’s being “classified” based on how many items they contain, 
# e.g., a 2-tuple would contain two items such as (some_key, some_value)

colors = ('red', 'green', 'blue')
colors_one = 'red', 'green', 'yellow'
print(type(colors)) #<class 'tuple'>
print(type(colors_one)) #<class 'tuple'>

create_tuple_one = "hello"
print(type(create_tuple_one)) #<class 'str'>
# If you need to create a 1-tuple (a tuple with one item), be aware that a comma is necessary:
create_tuple_two = "hello",
print(type(create_tuple_two)) #<class 'tuple'>


# ACCESSING ITEMS -> via bracket notation
print(colors[1])

# INDEXING -> Sequences (lists, tuples & strings) also have an index() method that returns the index of the first match:
print(colors.index("green"))

# ITERATION -> tuples are iterated over by using for...in loops
for color in colors:
    print(color)

# iteration with indexing:
    for idx, color in enumerate(colors):
        print(f"at {idx} position, we have {color} color")

# UNPACKING TUPLES
# Tuples (and other sequences such as lists & strings) have a convenient feature, called unpacking, 
# for performing multiple variable assignments in a single line of code:
        # COMMA SEPERATED variables on the LEFT_SIDE of the assignment operator and a sequence of values on the right is what it takes
        colors = ('red', 'green', 'blue')
        a,b,c = colors
        print(a,b,c)

        # same applies to lists
        m = [1,2,3]
        a,b,c, = m
        print(a)

        # same applies to strings
        word = "string"
        a,b,c,d, e, f = word
        print(f)
    

# SLICING (COPYING) SEQUENCES(STR, LIST, TUPLES)
        # Slicing in Python is used to create “slices” (copies) of sequences. -> a_sequence[m:n] -> lice includes up to, but not including the index to the right of the colon.

        my_name = "Solhjou Khah"
        short_name = my_name[0:7]
        print(short_name)

        # same applies to lists
        fruits = ["orange", "apple", "fig"]
        print(fruits[:2])

        # same applies to strings
        words = "hellohollymolly"
        print(words[6:])



# Essential Questions 
fruit = {
  'apples': 'red',
  'bananas': 'yellow',
  'oranges': 'orange'
}

color_of_bananas = fruit.get("bananas")
print(color_of_bananas)
if "bananas" in fruit:
    print(fruit["bananas"])

    