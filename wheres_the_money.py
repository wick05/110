###
### Author: Jake Wick
### Course: CSc 110
### Description: This program takes 5 inputs from the user, which are financial values used to create a
###              basic financial statement. If the user is spending more than their annual salary, it displays
###              a warning that they are operating at a deficit. If they are paying max tax, it also gives a disclaimer.

# printing the header/title of the program
print('-----------------------------')
print("----- WHERE'S THE MONEY -----")
print('-----------------------------')

# prompting user for annual salary, and making sure the string is a positive numerical integer
# if not, it displays an error and exits the program
annual_salary = input('What is your annual salary?\n')
if annual_salary.isnumeric() == 0:
    print('Must enter positive integer for salary.')
    exit()

# prompting user for monthly mortgage/rent cost, and making sure the string is a positive numerical integer
# if not, it displays an error and exits the program
monthly_mortgage = input('How much is your monthly mortgage or rent?\n')
if monthly_mortgage.isnumeric() == 0:
    print('Must enter positive integer for mortgage or rent.')
    exit()

# prompting user for monthly bills, and making sure the string is a positive numerical integer
# if not, it displays an error and exits the program
monthly_bills = input('What do you spend on bills monthly?\n')
if monthly_bills.isnumeric() == 0:
    print('Must enter positive integer for bills.')
    exit()

# prompting user for weekly food expenses, and making sure the string is a positive numerical integer
# if not, it displays an error and exits the program
weekly_food = input('What are your weekly grocery/food expenses?\n')
if weekly_food.isnumeric() == 0:
    print('Must enter positive integer for food.')
    exit()

# prompting user for annual travel expenses, and making sure the string is a positive numerical integer
# if not, it displays an error and exits the program
annual_travel = input('How much do you spend on travel annually?\n')
if annual_travel.isnumeric() == 0:
    print('Must enter positive integer for travel.')
    exit()

# converting annual salary from a string to an int, so we can do calculations on it
annual_salary = int(annual_salary)

# creating an annual mortgage variable by multiplying monthly mortgage by 12
annual_mortgage = int(monthly_mortgage)*12
# calculating the mortgage's share of annual income by dividing annual mortgage by annual salary
mortgage_percent = annual_mortgage/annual_salary

# creating an annual bills variable by multiplying monthly bills by 12
annual_bills = int(monthly_bills)*12
# calculating the mortgage's share of annual income by dividing annual bills by annual salary
bills_percent = annual_bills/annual_salary

# creating an annual food variable by multiplying weekly food by 52 (went with 52 instead of 52.1429)
annual_food = int(weekly_food)*52
# calculating the food's share of annual income by dividing annual food by annual salary
food_percent = annual_food/annual_salary

# converting annual travel from a string to an int
annual_travel = int(annual_travel)
# calculating the travel's share of annual income by dividing annual travel by annual salary
travel_percent = annual_travel/annual_salary

# calculating the annual amount of tax the user pays using conditional logic
# if the user's annual income falls in a particular bracket, the tax is calculated at the bracket's rate
if 0 <= annual_salary <= 15000:
    TAX_PERCENTAGE = 10
    annual_tax = annual_salary * (TAX_PERCENTAGE / 100.00)
elif 15000 < annual_salary <= 75000:
    TAX_PERCENTAGE = 20
    annual_tax = annual_salary * (TAX_PERCENTAGE / 100.00)
elif 75000 < annual_salary <= 200000:
    TAX_PERCENTAGE = 25
    annual_tax = annual_salary * (TAX_PERCENTAGE / 100.00)
else:
    TAX_PERCENTAGE = 30
    annual_tax = annual_salary * (TAX_PERCENTAGE / 100.00)

# if the amount of tax exceeds 75000, the value is reset to 75000
# also added a variable to use at the end of the program that is a marker that the tax limit has been reached
tax_limit_reached = 0
if annual_tax > 75000:
    annual_tax = 75000
    tax_limit_reached = 1

# calculating the tax's share of annual income by dividing annual tax by annual salary
# variable name is slightly different from other _percent variables, to not mistake it for TAX_PERCENTAGE
tax_percent_of_annual = annual_tax/annual_salary

# calculating the extra money left over at the end by subtracting all the expenses from the income
annual_extra = annual_salary - annual_mortgage - annual_bills - annual_food - annual_travel - annual_tax
# calculating the extra money's share of annual income by dividing annual extra money by annual salary
extra_percent = annual_extra/annual_salary

# adding a condition where if the money left over is negative, then the deficit_warning variable
# is switched to 1, which will let us know to display a warning at the end or not
deficit_warning = 0
if annual_extra < 0:
    deficit_warning = 1

# formatting the annual mortgage cost to take up 11 spaces, have commas, and have 2 decimals
formatted_mortgage = format(annual_mortgage, '11,.2f')
# formatting the mortgage_percent, which is a float [0, 1] to take up 7 spaces, have 1 decimal, and end with a % sign
formatted_mortgage_percent = format(mortgage_percent, '7.1%')
# calculating how many # pound signs to display based on the mortgage percent * 100
# converting it to an integer chops off any extra decimal place, effectively rounding it down
mortgage_pound = int(mortgage_percent * 100)
# combining the formatting of the table with these formatted variables into a single string variable
# this is necessary to determine the length of the entire row, and helps shorten the line of code when printing
row1 = ('| mortgage/rent | $' + formatted_mortgage + ' |' + formatted_mortgage_percent + ' | ' + mortgage_pound * '#')

# I used the formatting and same calculations from the mortgage section above on the rest of the variables:
# bills, food, travel, tax, and extra income. This allowed me to create a row string variable for each variable
formatted_bills = format(annual_bills, '11,.2f')
formatted_bills_percent = format(bills_percent, '7.1%')
bills_pound = int(bills_percent * 100)
row2 = ('|         bills | $' + formatted_bills + ' |' + formatted_bills_percent + ' | ' + bills_pound * '#')

formatted_food = format(annual_food, '11,.2f')
formatted_food_percent = format(food_percent, '7.1%')
food_pound = int(food_percent * 100)
row3 = ('|          food | $' + formatted_food + ' |' + formatted_food_percent + ' | ' + food_pound * '#')

formatted_travel = format(annual_travel, '11,.2f')
formatted_travel_percent = format(travel_percent, '7.1%')
travel_pound = int(travel_percent * 100)
row4 = ('|        travel | $' + formatted_travel + ' |' + formatted_travel_percent + ' | ' + travel_pound * '#')

formatted_tax = format(annual_tax, '11,.2f')
formatted_tax_percent = format(tax_percent_of_annual, '7.1%')
tax_pound = int(tax_percent_of_annual * 100)
row5 = ('|           tax | $' + formatted_tax + ' |' + formatted_tax_percent + ' | ' + tax_pound * '#')

formatted_extra = format(annual_extra, '11,.2f')
formatted_extra_percent = format(extra_percent, '7.1%')
extra_pound = int(extra_percent * 100)
row6 = ('|         extra | $' + formatted_extra + ' |' + formatted_extra_percent + ' | ' + extra_pound * '#')

# using the max() and len() functions to find which row is the longest, and setting that value to be
# how many dashes to use in the table at the end
dash_ui = max(len(row1), len(row2), len(row3), len(row4), len(row5), len(row6))

# printing the table
print('\n' + '-' * dash_ui)
print('See the financial breakdown below, based on a salary of $' + str(annual_salary))
print('-' * dash_ui)
print(row1)
print(row2)
print(row3)
print(row4)
print(row5)
print(row6)
print('-' * dash_ui)

# determining if we should print the deficit warning, based on the deficit_warning variable from earlier
if deficit_warning == 1:
    print('>>> WARNING: DEFICIT <<<')

# determining if we should print the tax limit disclaimer, based on the deficit_warning variable from earlier
if tax_limit_reached == 1:
    print('>>> TAX LIMIT REACHED <<<')