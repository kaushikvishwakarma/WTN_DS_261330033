def check_odd_even():
    try:
        number = int(input("Enter an integer: "))
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    check_odd_even()
