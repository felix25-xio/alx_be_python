# robust_division_calculator.py
def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Attempt the division
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
# main.py
import sys
from robust_division_calculator import safe_divide

def main():
    # Check for the correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Retrieve command-line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the division function and print the result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
