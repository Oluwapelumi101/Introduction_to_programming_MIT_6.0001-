# MIT course 6 problem set 1
# A program to calculate how many months one has to save for a house with a certain income and return on saving at a certian rate

# Taking User input
# annual_salary = int(input("How much do you earn yearly? "))
# portion_saved = int(input("What percentage of your Monthly Salary would you like to save? "))
# total_cost = int(input("How Much does our Dream Home Cosr? "))
# semi_annual_raise = int(input("By what percentage does your salary increase every 6 month? "))

# fixed test case
# annual_salary = 75000
# portion_saved = 5
# total_cost = 1500000
# semi_annual_raise = 5

# annual_salary = 120000
# portion_saved = 10
# total_cost = 1000000
# semi_annual_raise = 7

# Deductions
monthly_income = annual_salary / 12
portion_down_payment = total_cost * 0.25

# Return on savings
current_savings = 0
n = 0
while (current_savings < portion_down_payment):
    monthly_income = annual_salary / 12
    monthly_savings = monthly_income * portion_saved/100
    current_savings += monthly_savings + (current_savings * 0.04/12 )
    n += 1
    # print(n ,"|", monthly_income)
    if (n % 6 == 0) & (n != 0):
        annual_salary += annual_salary * (semi_annual_raise/100)
        # print(n ,"|", annual_salary)
print(n)
print(f"You would need to save {monthly_savings} for a total of {n} Months")