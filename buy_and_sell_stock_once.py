#Design an algorithm that determines the maximum profit that could have been made by buying and then selling a single share over a given day range, subject to the constraint that the buy and the sell have to take place at the start of the day; the sell must occur on a later day. 

#As an example: consider the following sequence of stock prices: {310, 315, 275, 295, 260, 270, 290, 230, 255, 250}. The maximum profit that can be made with one buy and one sell is 30 - buy at 260 and sell at 290. Note that 260 is not the lowest price, nor 290 the highest price. 

#input: Array denoting daily stock price
#output: Maximum profit that could be made by buying and selling one share of that stock

#Brute-force idea. Nested loops, if s[i] - s[j] is greater than the current max difference, update max difference


def buy_and_sell_stock_once_brute_force(daily_price): 
	maxDif = 0
	
	for i in range(len(daily_price)): 
		
		for j in range(i+1, len(daily_price)): 
			if daily_price[j] - daily_price[i] > maxDif: 
				maxDif = daily_price[j] - daily_price[i]
	return maxDif


print(buy_and_sell_stock_once_brute_force([310, 315, 275, 295, 260, 270, 290,230, 255, 250]))




