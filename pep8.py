# Good practice (PEP 8 compliant)
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Avoid (not PEP 8 compliant)
def CalculateAverage(numbers):
    Total = sum(numbers)
    AVERAGE = Total / len(numbers)
    return AVERAGE
