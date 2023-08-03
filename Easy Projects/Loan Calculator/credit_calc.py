import argparse
from math import ceil, log

# calculate loan interest for the two types of payments
def loan_interest_calc(loan_interest):
    loan_interest = loan_interest / (12*100)
    return loan_interest

# divide months to years and months
def months_to_years(months):
    years = months // 12
    months = months % 12
    return years, months
# calculate overpayment for the two types of payments
def over_payment(payments, loan_principal):
    over_payment = payments - loan_principal
    print(f"Overpayment = {int(over_payment)}") 

############ calculate differentiated payments ########################### 
def diff_calc(loan_principal, number_of_months, interest):
    p = loan_principal
    n = number_of_months
    loan_interest = i = loan_interest_calc(interest)
    payments = 0
    for m in range(1, number_of_months + 1):
        diff_payment = ceil(p / n + i * (p - (p * (m-1) / n)))
        payments += diff_payment
        print(f"Month {m}: payment is {diff_payment}")
    
    over_payment(payments, loan_principal)

########## calculate the three parameters for annuity payments ################
# annuity payments: calculate the monthly payment
def monthly_payment(loan_principal, number_of_months, interest):
    p = loan_principal
    n = number_of_months
    loan_interest = i = loan_interest_calc(interest)
    monthly_payment = ceil(p * ((i*((1+i)**n))/(((1+i)**n)-1)))
    payments = monthly_payment * number_of_months
    print(f"Your monthly payment = {monthly_payment}!")
    over_payment(payments, loan_principal)

# annuity payments: claculate the number of months
def number_of_monthly_payments(loan_principal, monthly_payment, interest):
    p = loan_principal
    a = monthly_payment
    loan_interest = i = loan_interest_calc(interest)
    number_of_months = ceil(log(a/(a-i*p)) / log (1+i))
    payments = monthly_payment * number_of_months
    print(payments)
    years, months = months_to_years(number_of_months)
    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    elif months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")
    
    over_payment(payments, loan_principal)

# annuity payments: calculate the loan principal
def loan_principal(monthly_payment, number_of_months, interest):
    a = monthly_payment
    n = number_of_months
    loan_interest = i = loan_interest_calc(interest)
    loan_principal = int(a / ((i*((1+i)**n)) / (((1+i)**n)-1)))
    payments = monthly_payment * number_of_months
    print(f"Your loan principal = {loan_principal}!")
    over_payment(payments, loan_principal)
    
######### the arguments that user enter for calculations ##############
    
def menu():
    # Ensure that arguments values are positive, it will return value only if it's positive
    def check_positive(value):
        value = float(value)        
        if value > 0:
            return value
    parser = argparse.ArgumentParser(prog="Loan Calculator", description="loan calculator for the two loan types: Annuity and Differentiated, you should follow the '--type' argument with other arguments depend on what you want to calculate!")

    parser.add_argument("--type", choices=["annuity", "diff"], help="Choose between the two choices for the loan type")
    parser.add_argument("--principal", type=check_positive, help="Enter the loan principal value")
    parser.add_argument("--periods", type=check_positive, help="Enter the number of months")
    parser.add_argument("--payment", type=check_positive, help="Enter the monthly payment")
    parser.add_argument("--interest", type=check_positive, help="Enter the loan interest")

    args=parser.parse_args()


    if args.type == "diff":
        if args.principal != None and args.periods != None and args.payment == None and args.interest != None:
            diff_calc(args.principal, int(args.periods), args.interest)
        else:
            print("Incorrect parameters")
    elif args.type == "annuity":
        if args.principal != None and args.periods != None and args.payment == None and args.interest != None:
            monthly_payment(args.principal, int(args.periods), args.interest)
        elif args.principal != None and args.periods == None and args.payment != None and args.interest != None:
            number_of_monthly_payments(args.principal, args.payment, args.interest)
        elif args.principal == None and args.periods != None and args.payment != None and args.interest != None:
            loan_principal(args.payment, int(args.periods), args.interest)
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")

menu()
