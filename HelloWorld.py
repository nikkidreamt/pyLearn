import json
import os

print("Hello World.")

x = 3
y = 10
z = y % x
print("z=" + str(z))

if x > y:
    print("x more then y")
else:
    print("y more then x")
animals = ["Cat", "Dog", "Mule", "Horse"]
print("2,3: " + str(animals[1:3]))
for index in animals:
    if index == "Cat":
        print("bingo!")
    print(index)

animals.remove("Mule")
del animals[0]

print("First is " + animals[0])    
print("Length is " + str(len(animals)))    

# input_var = input("Enter the animal: ")
# animals.append(input_var)
print(animals)

# if x == 10: 
#     print("something")

FIRST_dict = {"one": 1, "two": 2, "three": 3}
print(FIRST_dict["two"])

second_disc = {1: "one", 2: "two", 3: "htree"}

print(second_disc[2])

third_disc = {1: ["Horse", "Dog"], 2: ["Horse", "Cat"], 3: ["Mule"]}

print(third_disc[2])

for index in  range(2,10,2):
    print (index)
# Handle exceptions with a try/except block

# Handle exceptions with a try/except block
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass                 # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass                 # Multiple exceptions can be handled together, if required.
else:                    # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")   # Runs only if the code in try raises no exceptions
finally:                 #  Execute under all circumstances
    print("We can clean up resources here")

try:
    raise EOFError()
    raise IndexError("45345435")
except:
    pass


# contents = {"aa": 12, "bb": 21}
# with open("myfile1.txt", "w+") as file:
#     file.write(str(contents))        # writes a string to a file

with open("myfile1.txt") as file:
    content = json.load(file)
    print(content['aa'])

print(os.getcwd())    