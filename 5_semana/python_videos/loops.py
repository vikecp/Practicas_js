from itertools import count


foods = ["apples", "bread", "milk", "Cheese"]

for food in foods:
    if food == "Cheese":
        print("You have to but this")
    print(food)
    

# while
count = 4
while count <= 10:
    print(count)
    count = count  + 1