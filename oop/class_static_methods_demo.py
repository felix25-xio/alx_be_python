class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        #Static method to add two numbers.
        return a + b

    @classmethod
    def multiply(cls, a, b):
  #class method to multiply two numbers. Prints the class attribute before performing the multiplication.
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Example usage
def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"Sum: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"Product: {product_result}")

if __name__ == "__main__":
    main()
