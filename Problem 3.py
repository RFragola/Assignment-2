

def main():
    credit = int(input("Please enter your credit score: "))
    if credit < 300 or credit > 850:
        print("Invalid credit score. Please enter a score between 300 and 850.")
        print("")
        main()
        return
    income = float(input("Please enter your annual income: $"))

    if credit >= 720 and income >= 60000:
        print("Loan Risk Category: Low Risk")
        print("")
    elif credit >= 650 and income >= 40000:
        print("Loan Risk Category: Medium Risk")
        print("")
    else:
        print("Loan Risk Category: High Risk")
        print("")


main()