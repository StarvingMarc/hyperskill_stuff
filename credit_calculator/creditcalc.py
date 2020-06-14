from math import ceil
from math import log
from math import floor
import argparse
import textwrap

parser = argparse.ArgumentParser(description='Credit Calculator', formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('''\
                                 Annuity options:
                                    monthly payment:  --type=annuity --principal --periods --interest
                                    credit principal: --type=annuity --payment --periods --interest
                                    periods:          --type=annuity --principal --payment --interest
                                 
                                 Differentiated option:
                                    differentiated payment: --type=diff --principal --periods --interest:
                                 '''))
parser.add_argument('-t', '--type', metavar='', help='"=annuity" or "=diff"')
parser.add_argument('-p', '--payment', type=int, metavar='', help='monthly payment')
parser.add_argument('-P', '--principal', type=int, metavar='', help='principal amount')
parser.add_argument('-r', '--periods', type=int, metavar='', help='number of months to pay')
parser.add_argument('-i', '--interest', type=float, metavar='', help='interest rate, int or decimal')
args = parser.parse_args()


def count_of_months():
    nom_int = (args.interest / 100) / 12 * 1
    number_of_payments = ceil(log(args.payment / (args.payment - nom_int * args.principal), nom_int + 1))
    years = number_of_payments / 12
    years_to_pay = round(years // 1)
    month = round(12 * (years % 1))
    if years_to_pay == 1 and month != 1:
        print(f"You need {years_to_pay} year and {month} months to repay this credit!")
    elif years_to_pay != 1 and month != 1:
        print(f"You need {years_to_pay} years and {month} months to repay this credit!")
    elif years_to_pay == 1 and month == 1:
        print(f"You need {years_to_pay} year and {month} month to repay this credit!")
    else:
        print(f"You need {years_to_pay} years and {month} month to repay this credit!")
    print(f"Overpayment = {(number_of_payments * args.payment) - args.principal}")


def annuity_monthly_payment():
    nom_int = (args.interest / 100) / 12 * 1
    amp = ceil(args.principal * (nom_int * (pow(1 + nom_int, args.periods)) / (pow(1 + nom_int, args.periods) - 1)))
    print(f"Your annuity payment = {amp}!")
    print(f"Overpayment = {amp * args.periods - args.principal}")


def credit_principal():
    nom_int = (args.interest / 100) / 12 * 1
    ppl = floor(args.payment / (nom_int * (pow(1 + nom_int, args.periods)) / (pow(1 + nom_int, args.periods) - 1)))
    print(f"Your credit principal = {ppl}!")
    print(f"Overpayment = {(args.periods * args.payment) - ppl}")


def differentiated_payment():
    month_count = 1
    current_period = 1
    diff_list = []
    for i in range(int(args.periods)):
        nom_int = (args.interest / 100) / 12 * 1
        diff = ceil(args.principal / args.periods + (nom_int * (args.principal - (args.principal * (current_period - 1) / args.periods))))
        print(f"Month {month_count}: paid out {diff}")
        month_count += 1
        current_period += 1
        diff_list.append(diff)
    print()
    print(f"Overpayment = {sum(diff_list) - args.principal}")


if args.type == "annuity":
    if args.principal and args.periods and args.interest:
        annuity_monthly_payment()
    elif args.payment and args.periods and args.interest:
        credit_principal()
    elif args.principal and args.payment and args.interest:
        count_of_months()
    else:
        print("Incorrect parameters")
elif args.type == "diff":
    if args.principal and args.periods and args.interest:
        differentiated_payment()
    else:
        print("Incorrect parameters")

