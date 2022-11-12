# MIT course 6 problem set 1
# A program to calculate how many months one has to save for a house with a certain income and return on saving at a certian rate
# The program is to find the best saving rates to buy a house withing a fixed period using binary search


import math

# Taking User input
starting_salary = int(input("How much do you earn yearly? "))
total_cost = int(input("How Much does our Dream Home Cosr? "))
semi_annual_raise = int(input("By what percentage does your salary increase every 6 month? "))
duration = int(input('How many months would you like to spend saving? '))

# Some test inputs
# starting_salary = 120000
# portion_saved = 0
# total_cost = 1000000
# semi_annual_raise = 7

# starting_salary = 120000
# portion_saved = 0
# total_cost = 500000
# semi_annual_raise = 3

# starting_salary = 300000
# total_cost = 1000000
# semi_annual_raise = 7
# duration = 36

# Deductions
portion_down_payment = total_cost * 0.25
current_savings = 0
n = 0
start = 0
end = 10000
epsilon = 0.5
rate = (end + start) / 2.0
number_of_steps = 0

# Using Binary search
while abs(current_savings - portion_down_payment) >= epsilon:
    rate = (end + start) / 2.0
    portion_saved = rate/100
    current_savings = 0
    annual_salary = starting_salary
    number_of_steps += 1
    for n in range(duration):
        monthly_income = annual_salary / 12
        monthly_savings = monthly_income * portion_saved
        current_savings += monthly_savings + (current_savings * 0.04/12)
        if (n % 6 == 0) & (n != 0):
            annual_salary += annual_salary * (semi_annual_raise/100)
    # print(rate, "|", current_savings, "|", abs(current_savings - portion_down_payment ))
    if (current_savings < portion_down_payment):
        start = rate
    else:
        end = rate

print(f"You would need to save {round(rate, 2)}% of your monthly income to achieve your goal")
print(f"Number of Steps {number_of_steps}")



# # Using guess and check
# for i in range(2000):
#     portion_saved = i/100
#     current_savings = 0
#     annual_salary = starting_salary
#     for n in range(112):
#         monthly_income = annual_salary / 12
#         monthly_savings = monthly_income * portion_saved
#         current_savings += monthly_savings + (current_savings * 0.04/12)
#         # print(n ,"|", annual_salary, "|", starting_salary)
#         if (n % 6 == 0) & (n != 0):
#             annual_salary += annual_salary * (semi_annual_raise/100)
#             # print(n ,"|", annual_salary, "|", starting_salary)
#     if current_savings > portion_down_payment:
#         print(i)
#         print(monthly_savings)
#         print(portion_down_payment)
#         print(current_savings)
#     if current_savings > portion_down_payment:
#         break
  