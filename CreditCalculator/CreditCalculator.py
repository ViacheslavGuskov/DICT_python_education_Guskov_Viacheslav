import math

# Этап 1. Текстовые сообщения калькулятора.
print("Loan principal: 1000\nMonth 1: repaid 250\nMonth 2: repaid 250\nMonth 3: repaid 500\nThe loan has been repaid!")

# Этап 2. Расчёт кредита
print("Enter the loan principal:")
total_pay = float(input("> "))
print("""What do you want to calculate?\ntype "m" – for number of monthly payments,\ntype "p" – for the monthly payment:""")
type_inp = input("> ")
if type_inp == "m":
    print("Enter the monthly payment:")
    one_months = int(input("> "))
    number_months = math.ceil(total_pay / one_months)
    print("It will take " + str(number_months) + " months to repay the loan")
if type_inp == "p":
    print("Enter the number of months:")
    number_months = int(input("> "))
    one_months = math.ceil(total_pay / number_months)
    last_pay = total_pay - (number_months - 1) * one_months
    if last_pay == one_months:
        print("Your monthly payment = " + str(one_months))
    else:
        print("Your monthly payment = " + str(one_months) + " and the last payment = " + str(last_pay) + ".")