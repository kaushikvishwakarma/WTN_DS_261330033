def check_number():
    try:
        number = float(input("Enter a number: "))
        if number > 0:
            print("Positive")
        elif number < 0:
            print("Negative")
        else:
            print("Zero")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    check_number()
