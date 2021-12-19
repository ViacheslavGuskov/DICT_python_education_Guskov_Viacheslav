import math

# Этап 1. Текстовые сообщения калькулятора.
print("Loan principal: 1000\nMonth 1: repaid 250\nMonth 2: repaid 250\nMonth 3: repaid 500\nThe loan has been repaid!")

# Этап 2-3. Расчёт кредита
print("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")
type_inp = input("> ")
if type_inp == "n":
    print("Enter the loan principal:")
    loan_principal = float(input("> "))
    print("Enter the monthly payment:")
    monthly_payment = float(input("> "))
    print("Enter the loan interest:")
    loan_interest = float(input("> "))
    mounths_count = math.ceil(math.log(monthly_payment / (monthly_payment - (loan_interest / 1200 * loan_principal)), (1 + loan_interest / 1200)))
    if mounths_count // 12 == 0:
        info_date = str(mounths_count) + " months"
    if mounths_count % 12 == 0:
        info_date = str(mounths_count // 12) + " years"
    if mounths_count % 12 != 0:
        info_date = str(mounths_count // 12) + " years and " + str(mounths_count % 12) + " months"
    print("It will take " + info_date + " to repay this loan!")
if type_inp == "a":
    print("Enter the loan principal:")
    loan_principal = float(input("> "))
    print("Enter the number of periods:")
    number_periods = float(input("> "))
    print("Enter the loan interest:")
    loan_interest = float(input("> "))
    monthly_payment = math.ceil(loan_principal * ((loan_interest / 1200) * ((1 + loan_interest / 1200) ** number_periods) / (((1 + loan_interest / 1200) ** number_periods) - 1)))
    print("Your monthly payment = " + str(monthly_payment) + "!")
if type_inp == "p":
    print("Enter the annuity payment:")
    annuity_payment = float(input("> "))
    print("Enter the number of periods:")
    number_periods = float(input("> "))
    print("Enter the loan interest:")
    loan_interest = float(input("> "))
    loan_principal = round(annuity_payment / ((loan_interest / 1200) * ((1 + loan_interest / 1200) ** number_periods) / (((1 + loan_interest / 1200) ** number_periods) - 1)))
    print("Your loan principal = " + str(loan_principal) + "!")