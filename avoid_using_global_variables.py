# Good practice
def calculate_total_price(prices):
    total = sum(prices)
    return total

# Avoid
total = 0

def calculate_total_price(prices):
    global total
    total = sum(prices)
