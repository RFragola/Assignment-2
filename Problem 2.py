

def main():
    salary = float(input("Please enter your annual salary: $"))
    score = int(input("Please enter your performance score (0-100): "))
    # Restart is score is invalid
    if 0 > score or score > 100:
        print("Invalid performance score. Please enter a score between 0 and 100.")
        print("")
        main()
        return
    # Bonus calculation
    elif score >= 90:
        bonus = .20  # 10% bonus for scores 90 and above
    elif score >= 80:
        bonus = .10  # 10% bonus for scores between 80 and 89
    elif score >= 70:
        bonus = .05  # 5% bonus for scores between 70 and 79
    else:
        bonus = 0  # No bonus for scores below 70

    # Bonus math
    total_salary = salary + (salary * bonus)
    if bonus > 0:
        print(f"Congratulations! You're eligible for a {bonus * 100}% performance bonus!")
        print(f"Total Salary with Bonus: ${total_salary:.2f}")
    else:
        print("Unfortunately, you are not eligible for a bonus this year.")
        print(f"Total Salary: ${total_salary:.2f}")

main()