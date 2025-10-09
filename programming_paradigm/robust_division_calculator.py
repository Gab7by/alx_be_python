def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling division by zero
    and non-numeric input errors.
    """

    try:
        # Try converting both inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Try performing the division
        result = num / den
        return f"Result: {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Both inputs must be numeric values."
    except Exception as e:
        # Generic catch for unexpected errors
        return f"An unexpected error occurred: {e}"
