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


