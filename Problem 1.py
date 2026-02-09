


def main():
    purchase = float(input("Enter the total purchase amount: $"))
    member = input("Are you a member of our loyalty program? (yes/no): ").strip().lower()
    if member == 'yes':
        if purchase >= 100:
            discount = 0.15  # 15% discount for members with purchases of $100 or more
        elif 0 < purchase < 100:
            discount = 0.05  # 5% discount for members with purchases less than $100
        else: 
            print("Invalid purchase amount. Please enter a positive number.")
    else:
        if purchase >= 150:
            discount = 0.10  # 10% discount for non-members with purchases of $100 or more
        elif 0 < purchase < 150:
            discount = 0.00  # No discount for non-members with purchases less than $100
        else:
            print("Invalid purchase amount. Please enter a positive number.")
    # calculate discount and print result
    if discount > 0:
        print(f"Congratulations! You are eligible for a {discount * 100}% discount!")
        print(f"Your total after discount is: ${purchase * (1 - discount):.2f}")
        print("Thank you for shopping with us!")
    else:
        print("Thank you for shopping with us! Unfortunately, you are not eligible for a discount today.")
        print("Your total is: ${:.2f}".format(purchase))

main()
