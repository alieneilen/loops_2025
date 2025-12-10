# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]
print (len(fruits))

# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])
for fruit in fruits:
    print(fruit)    
# i just worked with loops

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
    print(subject)
for subject in subjects:
    if subject == "History":
        break #stops the list from printing 
    print(subject)

for subject in subjects: 
    if subject == "Science":
        continue #skips over science but continues with the rest of the list
    print (subject)

list1000 = list(range(1,1001))
for num in list1000: 
    if num > 599: 
        break
    print (num)

for num in list1000:
    if num > 300 and num < 500:
        continue #skips numbers between 300 and 500
    print (num)

# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"


# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.