#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("\n\nWelcome to the tip calculator.")
total_bill = float(input("What was the total bill? $" ))
perc_tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
n_people = int(input("How many people to split the bill? "))

total_bill += total_bill * (perc_tip / 100)
individual_bill = total_bill / n_people
individual_bill = round(individual_bill, 2)

print(f"Each person should pay: ${individual_bill}\n\n")

