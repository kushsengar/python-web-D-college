def valNum():
    try:
        n = float(input("Enter numeric value :"))
        return n
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

valNum()