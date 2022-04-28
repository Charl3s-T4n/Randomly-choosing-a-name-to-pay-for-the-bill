# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

#Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")        #Split the names into a list

#Get total no. of items in the list
num_items = len(names)
#Generate random number between range specified 
random_choice = random.randint(0, num_items - 1)  #Start and end included
selected_name = names[random_choice]

print(f"{selected_name} is going to buy the meal today!")
