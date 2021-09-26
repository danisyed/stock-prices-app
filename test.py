#   Copyright (c) 2021 www.SyedAdnan.com
#   Unit-testing using PyTest
#   This set of tests will unit test the application with 
#   different possible stock prices to make sure that code works properly
from app import get_max_profit, check_integer_prices

# UnitTest: Function should return integer
def test_integer_return():
   prices = [1, 2, 3]
   profit = get_max_profit(prices)
   assert type(profit) == int

# UnitTest: Function should not fail for empty List
def test_empty_list():
   prices = []
   profit = get_max_profit(prices)
   assert profit == 0

# UnitTest: Function should accept all integer prices
def test_int_list():
   prices = [1, 2, 3, 'something']
   profit = get_max_profit(prices)
   assert profit == 0

# UnitTest: Mid say purchase sale - Straight prices
def test_profit_random():
   prices = [10, 7, 5, 8, 11, 9]
   profit = get_max_profit(prices)
   assert profit == 6
 
# UnitTest: Stock Prices that goes in loss
def test_loss():
   prices = [11, 10, 9, 8, 2, 1]
   profit = get_max_profit(prices)
   assert profit == -1

# UnitTest: Buying in start and sell for max profit
def test_max_profit():
   prices = [1, 10, 7, 14, 2, 11]
   profit = get_max_profit(prices)
   assert profit == 13

# UnitTest: Stock Prices that has no profit no loss
def test_zero_profit():
   prices = [1, 1, 1, 1, 1, 1]
   profit = get_max_profit(prices)
   assert profit == 0

# UnitTest: Test the individual function
def test_indiv_function():
   prices = [1, 2, 3, 'something']
   profit = check_integer_prices(prices)
   assert profit == False