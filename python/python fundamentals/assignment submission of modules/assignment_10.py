def check_palindrome():
    try:
        number = int(input("Enter a number: "))
        original = number
        
        # Handle negative numbers for palindrome checks (usually not considered palindromes if we strictly match characters, but here we'll just work with absolute values or assume positive input based on examples)
        temp = abs(number)
        
        reversed_number = 0
        while temp > 0:
            digit = temp % 10
            reversed_number = reversed_number * 10 + digit
            temp = temp // 10
        
        # Adjust sign if it was negative
        if number < 0:
            reversed_number = -reversed_number
            
        if original == reversed_number:
            print(f"{original} is a palindrome.")
        else:
            print(f"{original} is not a palindrome.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    check_palindrome()
