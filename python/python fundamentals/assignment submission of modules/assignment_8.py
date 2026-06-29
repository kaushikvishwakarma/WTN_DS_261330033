def sum_of_digits():
    try:
        number_str = input("Enter a number: ")
        # Convert to int to use while loop logic as requested by topic "while"
        number = int(number_str)
        if number < 0:
            number = -number
            
        sum_digits = 0
        while number > 0:
            digit = number % 10
            sum_digits += digit
            number = number // 10
        print(sum_digits)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    sum_of_digits()
