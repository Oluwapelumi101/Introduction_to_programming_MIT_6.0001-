# MIT course 6 problem set 1
# A program to calculate how many months one has to save for a house with a certain income and return on saving at a certian rate

# Taking User input
# annual_salary = int(input("How much do you earn yearly? "))
# portion_saved = int(input("What percentage of your Monthly Salary would you like to save? "))
# total_cost = int(input("How Much does our Dream Home Cosr? "))

annual_salary = 120000
portion_saved = 10
total_cost = 1000000

# semi_annual_raise = 7
# Deductions
monthly_income = annual_salary / 12
portion_down_payment = total_cost * 0.25
monthly_savings = monthly_income * portion_saved/100

# Return on savings
current_savings = 0
n = 0

# Saving increase
while (current_savings < portion_down_payment):
    current_savings += monthly_savings + (current_savings * 0.04/12 )
    n += 1
    # print(current_savings)

print(current_savings)
print(f"You would need to save {monthly_savings} for a total of {n} Months")