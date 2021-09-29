#   Copyright (c) 2021 www.SyedAdnan.com
#   Title:   Function to calculate max profit from stock prices
#   Purpose: Coding exercies for Latitude
#   Author:  Syed Adnan
#   Date:    26 Sep, 2021

def get_max_profit(prices):
    """Accept stock prices and return max profit after evaluation

    Parameters
    ----------
    prices : list
        Stock prices from yesterday as list of integers
    Returns
    -------
    int
        An integer value of the max profit
    """

    # Validate if prices are passed
    if len(prices)==0 or len(prices) < 2:
        return 0

    # Validate if all prices are integer
    if not check_integer_prices(prices):
        return 0

    # Get stock buying and selling values from start of the day.
    max_profit = prices[1] - prices[0]
    low = prices[0]

    # Iterating the prices values to evaluate
    for i in prices:

        # Skip the first price in list
        if prices[0] == i:
            continue

        potential_profit = i - low
        max_profit= max(max_profit, potential_profit)
        low = min(low, i)
    
    # Returning the max_profit value
    return max_profit

def check_integer_prices(prices):
    """Validate if all stock prices values are integer

    Parameters
    ----------
    prices : list
        Stock prices from yesterday as list
    Returns
    -------
    Boolean
        True if all values are int, else False
    """
    return True if all(isinstance(x, int) for x in prices) else False

