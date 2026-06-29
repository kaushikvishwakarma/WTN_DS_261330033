def lastDigit(a, b):
    if a < 0 or b < 0:
        return False
    return (a % 10) == (b % 10)

if __name__ == "__main__":
    print(f"lastDigit(7, 17) -> {str(lastDigit(7, 17)).lower()}")
    print(f"lastDigit(6, 17) -> {str(lastDigit(6, 17)).lower()}")
    print(f"lastDigit(3, 113) -> {str(lastDigit(3, 113)).lower()}")
