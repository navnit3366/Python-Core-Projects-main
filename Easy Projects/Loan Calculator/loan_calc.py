# a simple calculator for Annuity Loan Payment
# it's calculate montly payment, number of months, loan principal
# if you want to calculate one from the above you should provide the others

from math import ceil, log

def loan_interest_calc():
    loan_interest = float(input("Enter the loan interest:"))
    loan_interest = loan_interest / (12*100)
    return loan_interest

def months_to_years(months):
    years = months // 12
    months = months % 12
    return years, months

def number_of_monthly_payments():
    loan_principal = p = int(input("Enter the loan principal:"))
    monthly_payment = a = float(input("Enter the monthly payment:"))
    loan_interest = i = loan_interest_calc()
    number_of_months = ceil(log(a/(a-i*p)) / log (1+i))
    years, months = months_to_years(number_of_months)
    
    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    elif months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")
    ### commented code below left for a future feature ###
    #if number_of_months == 1:
    #    print(f"It will take {ceil(number_of_months)} month to repay the loan")
    #else:
    #    print(f"It will take {ceil(number_of_months)} months to repay the loan")
    
def monthly_payment():
    loan_principal = p = int(input("Enter the loan principal:"))
    number_of_months = n = int(input("Enter the number of months:"))
    loan_interest = i = loan_interest_calc()
    monthly_payment = ceil(p * ((i*((1+i)**n))/(((1+i)**n)-1)))
    print(f"Your monthly payment = {monthly_payment}!")
    
    ### commented code below left for a future feature ###
    # last_payment = loan_principal - (number_of_months - 1) * ceil(monthly_payment)
    #if monthly_payment == int(monthly_payment):
    #    print(f"Your monthly payment = {int(monthly_payment)}")
    #else:
    #    print(f"Your monthly payment = {ceil(monthly_payment)} and the last payment = {last_payment}.")

# still not ready
def loan_principal():
    monthly_payment = a = float(input("Enter the monthly payment:"))
    number_of_months = n = int(input("Enter the number of months:"))
    loan_interest = i = loan_interest_calc()
    loan_principal = int(a / ((i*((1+i)**n)) / (((1+i)**n)-1)))
    print(f"Your loan principal = {loan_principal}!")

def menu():
    print("""What do you want to calculate?
    type "n" for number of monthly payments,
    type "a" for annuity monthly payment amount,
    type "p" for loan principal:""")
    print("If you want to exit just type 'exit'")
    choices = ['n', 'a', 'p', 'exit']
    choice = input()
    while choice in choices:
        if choice == 'n':
            number_of_monthly_payments()
            break
        elif choice == 'a':
            monthly_payment()
            break
        elif choice == 'p':
            loan_principal()
            break
        else:
            print("Nice to see you, have a nice day!")
            break
    else:
        print("\nInvald choice!")
        print("Try again.....'")
        menu()
menu()    
