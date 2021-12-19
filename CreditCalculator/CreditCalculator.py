# Этап 4. Расчёт кредита по заданным параметрам через аргументы командной строки.
import math
import argparse

def annuity_periods_C(loan_principal, monthly_payment, loan_interest):
    mounths_count = math.ceil(math.log(monthly_payment / (monthly_payment - (loan_interest / 1200 * loan_principal)), (1 + loan_interest / 1200)))
    if mounths_count // 12 == 0:
        info_date = str(mounths_count) + " months"
    if mounths_count % 12 == 0:
        info_date = str(mounths_count // 12) + " years"
    if mounths_count % 12 != 0:
        info_date = str(mounths_count // 12) + " years and " + str(mounths_count % 12) + " months"
    print("It will take " + info_date + " to repay this loan!")
    print("Overpayment = " + str(int(monthly_payment * mounths_count - loan_principal)))

def annuity_principal_C(monthly_payment, number_periods, loan_interest):
    loan_principal = round(monthly_payment / ((loan_interest / 1200) * ((1 + loan_interest / 1200) ** number_periods) / (((1 + loan_interest / 1200) ** number_periods) - 1)))
    print("Your loan principal = " + str(loan_principal) + "!")
    print("Overpayment = " + str(int(monthly_payment * number_periods - loan_principal)))

def annuity_payment_C(loan_principal, number_periods, loan_interest):
    monthly_payment = math.ceil(loan_principal * ((loan_interest / 1200) * ((1 + loan_interest / 1200) ** number_periods) / (((1 + loan_interest / 1200) ** number_periods) - 1)))
    print("Your monthly payment = " + str(monthly_payment) + "!")
    print("Overpayment = " + str(int(monthly_payment * number_periods - loan_principal)))

def annuity_C(interest, principal, periods, payment):
    if periods == None:
        annuity_periods_C(principal, payment, interest)
    if principal == None:
        annuity_principal_C(payment, periods , interest)
    if payment == None:
        annuity_payment_C(principal, periods, interest)

def diff_C(loan_interest, loan_principal, number_periods):
    main_duty = 0
    for mounth_num in range(1, number_periods + 1):
        differ_payment = math.ceil(float(loan_principal / number_periods) + (loan_interest / 1200) * (loan_principal - loan_principal * (mounth_num - 1) / number_periods))
        print('Month ' + str(mounth_num) + ': payment is ' + str(differ_payment))
        main_duty += differ_payment
    print('Overpayment = ' + str(int(main_duty - loan_principal)))

parser = argparse.ArgumentParser(description='CreditCalc')
parser.add_argument('--type', type=str)
parser.add_argument('--payment', type=float)
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
args = parser.parse_args()

if args.type == "annuity":
    if args.interest != None:
        if (args.principal != None and args.periods != None) or (args.principal != None and args.payment != None) or (args.periods != None and args.payment != None):
            annuity_C(args.interest, args.principal, args.periods, args.payment)
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
elif args.type == "diff":
    if args.payment == None and args.interest != None and args.principal != None and args.periods != None:
        diff_C(args.interest, args.principal, args.periods)
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")