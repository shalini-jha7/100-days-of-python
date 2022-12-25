# this program calculates the final amout to be paid per person along with tip
#Round the result to 2 decimal places
print("Welcome to the tip calculator!")
totalbill = int(input("What was the total bill?"))
tip = float(input("How much % tip would you like to give? 10, 12, or 15?"))
n = int(input("How many people to split the bill?"))
tip_percent = tip/100
tipamount = totalbill*tip_percent
pay_per_person = float((totalbill + tipamount)/n)
final_amount = round(pay_per_person, 2)
print("Each person should pay:",final_amount)

