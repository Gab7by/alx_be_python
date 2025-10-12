class Calculator:
    # Class attribute shared by all instances and referenced by the class method
    calculation_type = "Arithmetic Operations"

    # Static Method
    @staticmethod
    def add(a, b):
        """Return the sum of two numbers. Does not depend on class or instance."""
        return a + b

    # Class Method
    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers. Has access to class attributes."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
