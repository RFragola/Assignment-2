

def main():
    credit = int(input("Please enter your credit score: "))
    if credit < 300 or credit > 850:
        print("Invalid credit score. Please enter a score between 300 and 850.")
        print("")
        main()
        return
    income = float(input("Please enter your annual income: $"))

    if credit >= 720 and income >= 60000:
        risk = "Low Risk"
    elif credit >= 650 and income >= 40000:
        risk = "Medium Risk"
    else:
        risk = "High Risk"
    print("")
    print(f"Loan Risk Category: {risk}")


main()