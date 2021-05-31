def max_profit(prices):
	max_profit, min_price = 0, float('inf')
	for price in prices:
		min_price = min(min_price, price)
		profit = price - min_price
		max_profit = max(max_profit, profit)
	return max_profit

prices = [7,1,5,3,6,4]
print(max_profit(prices))
