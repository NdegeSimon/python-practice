#name=input("What is your name? ")
#age=int(input("What is your age? "))

#age=age+1

#print(f"Hello {name}, you are {age} years old!  Cheers HAPPY BIRTHDAY to you we wish you a prosperous year.")

# Python The area of a triangle is 

#length=int(input("The length of a rectangle is: "))
#width=int(input("the Width of a rectangle is: "))
#area=length*width

#print (f"the area of the rectangle is {area}cm")



#Example2
#Age=input("What is your Age?")
#if Age>="18":
    #print(f"You are an adult Your age is {Age}")
#else:
 #   print(f"You are a minor Your age is {Age}")

#Example3
#word = input("Enter a word: ")
#print("The word has", len(word), "letters.")

#example 3
#item = input("What do you want: ")
#price = float(input("What's the price of this item: "))
#quantity = int(input("How many do you want: "))

#total_price = quantity * price
#print(f"Total price for {quantity} {item}(s): ${total_price:.2f}")

# arithmetic operations


#result=round(x)
#result=pow(z, y)


#Example 5

#Circumference of a circle 
#import math

#radius= float(input("Enter the radius :"))
#circumference= 2*math.pi*radius
#print(f"The circumference of the circle is {circumference:.2f}")

# import math

#num1 = int(input("Input first number: "))
#num2 = int(input("Input second number: "))
#num3 = int(input("Input third number: "))
#average = (num1 + num2 + num3) / 3

#print(f"The average is {average:.2f}")  # Removed the equals sign after print

# Example 6: Even or odd number

#number = int(input("input number: "))

#if number % 2==0:
   # print(f"{number} is an even number")
#else:
    #print(f"{number} is an odd number")

# Example 7: Convert Celsius to Fahrenheit

#temperature_celsius = float(input("Enter temperature in Celsius: "))
#temperature_fahrenheit = (temperature_celsius * 9/5) + 32

#print(f"{temperature_celsius}°C is equal to {temperature_fahrenheit:.2f}°F")

# import math

# radius= float(input("Enter the radius of the circle:  "))
# area = math.pi * radius**2
# print(f"The area of the circle is {area:.2f}")

# This is a simple calculator program that performs basic arithmetic operations


# operator = input("Enter Operator(+, -, *, /): ")


# num1= float(input("Enter The First Number: "))
# num2=float(input("Enter the Second Number: "))

# if operator =="+":
#     result = num1 + num2
#     print(f"The result of {num1} + {num2} is {result}")

# elif operator =="-":
#     result = num1 - num2
#     print(f"The result of {num1} - {num2} is {result}")

# elif operator =="*":
#     result = num1 * num2
#     print(f"The result of {num1} * {num2} is {result}")

# elif operator =="/":
#     if num2 != 0:
#         result = num1 / num2
#         print(f"The result of {num1} / {num2} is {result}")
#     else:
#         print("Error: Division by zero is not allowed.")

# else:
#     print("Invalid operator. Please use +, -, *, or /.")


#MAx Number
# a = 7
# b = 5

# max_number = a if a > b else b

# print(f"The maximum number between {a} and {b} is {max_number}")

# Age = 17
# if Age >= 18:
#     print("You can get in the Club  You are an adult")
# else:
#     print("You are a minor no Entrance to the club")
#
# Weather = 32
# Weather = "HOT" if Weather >= 30 else "COLD"

# print(f"the weather today is {Weather}")

# Exercise1

# name = input("What is your name? ")  # Prompt for name
# if len(name) == 0 or name.isspace():  # Check for empty or all-space input
#     print("Error: Name cannot be empty or contain only spaces.")
# elif " " in name:  # Check for any spaces
#     print("Error: Name cannot contain spaces.")
# elif any(char.isdigit() for char in name):  # Check for any digits
#     print("Error: Name cannot contain digits.")
# elif len(name) > 12:  # Check if name exceeds 12 characters
#     print("Error: Name cannot exceed 12 characters.")
# else:  # If all checks pass, proceed to age input
#     try:
#         age = int(input("What is your age? "))  # Prompt for age and convert to int
#         age = age + 1  # Increment age for birthday
#         print(f"SignUp Successful! Hello {name}, you are {age} years old! Cheers HAPPY BIRTHDAY to you, we wish you a prosperous year.")
#     except ValueError:  # Handle non-numeric age input
#         print("Error: Please enter a valid number for age.")


#While Loop

# age = int(input("Enter Your Age: "))
# while age < 18:
#     print("Verification not Successful")
#     age = int(input("Enter Your Age: "))
# else:
#     print("Verification Successful")

# num= int(input("Enter a number between 1 and 100: "))

# while num < 1 or num > 100:
#     print(f"{num} is not"))


#For Loop
# import time

# my_time = int(input("How many hours do you want to sleep: "))
# total_seconds = my_time * 3600  # Convert hours to seconds

# for x in range(total_seconds, 0, -1):
#     hours = x // 3600
#     minutes = (x % 3600) // 60
#     seconds = x % 60
#     print(f"{hours:02}:{minutes:02}:{seconds:02} HRS")
#     time.sleep(1)

# print("Wake Up!")


# Example PostFix-Expresion

# import math
# num1=float(input("Enter num one"))
# num2=float(input("Enter num two"))
# operator=input("Enter operator (+, -, *, /): ")



# evaluate_postfix=(f"{num1},{num2},{operator}")

# foods=[]
# prices=[]
# total=0

# while True:
#     food= input("Enter Food to buy(q to quit): ")
#     if food.lower()=="q":
#       break
#     else:
#       foods.append(food)
#       price= float(input(f"Enter Price of {food}: "))
#       prices.append(price)
#       total+=price
# print("-----YOUR CART----")
# print("Your Order:")
# for i in range(len(foods)):
#     print(f"{foods[i]} - ${prices[i]:.2f}")

# print(f"Total Amount: ${total:.2f}")

# students = []
# scores = []
# total_score = 0

# print("=== STUDENT GRADE TRACKER ===")
# print("Enter student names and their test scores.")
# print("Type 'done' when finished.\n")

# while True:
#     student_name = input("Enter student name: ").strip()
    
#     if student_name.lower() == "done":
#         break
    
#     if student_name == "":
#         print("Please enter a valid name.")
#         continue
    
#     try:
#         score = float(input(f"Enter {student_name}'s test score: "))
        
#         if score < 0:
#             print("Score cannot be negative. Please try again.")
#             continue
            
#         students.append(student_name)
#         scores.append(score)
#         total_score += score
        
#     except ValueError:
#         print("Please enter a valid number for the score.")
#         continue

# print("\n" + "="*40)
# print("CLASS PERFORMANCE REPORT")
# print("="*40)

# if len(students) == 0:
#     print("No students were entered.")
# else:
#     print(f"\nTotal Students: {len(students)}")
    
#     print("\nIndividual Scores:")
#     print("-" * 25)
#     for i in range(len(students)):
#         print(f"{students[i]:<15} : {scores[i]:>6.1f}")
    
#     class_average = total_score / len(students)
#     print(f"\nClass Average: {class_average:.2f}")
    
#     if scores:
#         highest_score = max(scores)
#         lowest_score = min(scores)
#         highest_student = students[scores.index(highest_score)]
#         lowest_student = students[scores.index(lowest_score)]
        
#         print(f"Highest Score: {highest_score:.1f} ({highest_student})")
#         print(f"Lowest Score : {lowest_score:.1f} ({lowest_student})")
        
#         # Grade distribution
#         a_count = sum(1 for score in scores if score >= 90)
#         b_count = sum(1 for score in scores if 80 <= score < 90)
#         c_count = sum(1 for score in scores if 70 <= score < 80)
#         d_count = sum(1 for score in scores if 60 <= score < 70)
#         f_count = sum(1 for score in scores if score < 60)
        
#         print(f"\nGrade Distribution:")
#         print(f"A (90+)  : {a_count} students")
#         print(f"B (80-89): {b_count} students") 
#         print(f"C (70-79): {c_count} students")
#         print(f"D (60-69): {d_count} students")
#         print(f"F (<60)  : {f_count} students")

# print("\nThank you for using the Grade Tracker!")

# Example numbers PAD

# num_pad=((1,2,3),
#          (4,5,6),
#          (7,8,9),
#          ("*",0,"#"))

# for row in num_pad:
#    for num in row:
#       print(num, end="  ")
#       print()
# questions = ("What's the name of this Country:",
#            "Which County is Amboseli Located:",
#            "Best island to Visit in Africa:",
#            "What's the World's Population:",
#            "What company owns ChatGPT:")

# options = (("A. Kenya", "B. Mombasa", "C. Tanzania", "D. Kasongo"),
#           ("A. Kajiado", "B. Kisumu", "C. Nairobi", "D. Juba"),
#           ("A. Zanzibar", "B. Eldoret", "C. Busia", "D. Kisumu"),
#           ("A. 7 trillion", "B. 8 billion", "C. 1 Million", "D. 5656"),
#           ("A. OpenAI", "B. ChatGPT", "C. Google", "D. LinkedIn"))

# answers = ("A", "A", "A", "B", "A")
# score = 0

# for i in range(len(questions)):
#     print(f"\n{questions[i]}")
#     for option in options[i]:
#         print(option)
    
#     guess = input("Your answer (A, B, C, D): ").upper()
    
#     if guess == answers[i]:
#         print("Correct!")
#         score += 1
#     else:
#         print(f"Wrong! Answer was {answers[i]}")

# print(f"\nFinal Score: {score}/{len(questions)}")

# DICTIONARIES IN PYTHON

# capitals={
#     "Kenya":"Nairobi",
#     "Uganda":"Kampala",
#     "Tanzania":"Dodoma",
#     "Rwanda":"Kigali",
#     "Burundi":"Gitega"

# }



# print(capitals.get("Kenya"))

# # capitals.pop("Burundi")
# # print(capitals)

# capitals.update({"Ethiopia":"Addis Ababa"})
# print(capitals)
import random

# Dice ASCII art
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")
}

dice = []
total = 0

num_of_dice = int(input("How many dice? "))

# Roll the dice
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

print(f"\nYou rolled: {dice}")

# Display dice art
print("\nDice:")
for i in range(5):  # Each dice art has 5 lines
    for die_value in dice:
        print(dice_art[die_value][i], end="  ")  # Print side by side
    print()  # New line after each row

# Calculate total
for die in dice:
    total += die

print(f"\nTotal: {total}")