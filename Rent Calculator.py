#Making Project of Rent Calculator
##inputs we need from the user
#Total rent 
# Total food ordered for snacking
#electricity units spend
# charge per unit
#persons living in room/flat

## output
#total amount you've to pay is

rent = int(input("Enter your room/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enetr the number of persons living in the room/flat = "))

total_bill = electricity_spend * charge_per_unit
output = (food + rent + total_bill) // persons
print("Each person will pay : ",output)

# finish our beginner project in python .....code by tasleem sulthana

#example of displaying /output after executing the program of rent calculator

#Enter your room/flat rent = 7000
#Enter the amount of food ordered = 3000
#Enter the total electricity spend = 870
#Enter the charge per unit = 11
#Enetr the number of persons living in the room/flat = 5
#Each person will pay :  3914
