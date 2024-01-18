class CalculationError(Exception):
    """Exception raised for calculation errors.
    (divide by zero, root for negative...)

    Attributes:
        message - explanation of the error
    """
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message
