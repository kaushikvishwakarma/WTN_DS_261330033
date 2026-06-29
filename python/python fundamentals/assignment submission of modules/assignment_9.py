def reverse_number():
    try:
        number = int(input("Enter a number: "))
        
        is_negative = False
        if number < 0:
            is_negative = True
            number = -number
            
        reversed_number = 0
        while number > 0:
            digit = number % 10
            reversed_number = reversed_number * 10 + digit
            number = number // 10
            
        if is_negative:
            reversed_number = -reversed_number
            
        print(reversed_number)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    reverse_number()
