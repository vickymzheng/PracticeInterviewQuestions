def brute_force(prices):    
    max_profit = 0
    buy_day = -1
    sell_day = -1 
    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit: 
                max_profit = profit
                buy_day = i 
                sell_day = j 
    return [buy_day, sell_day, max_profit]

# [100, 150, 300, 40, 500, 700] # prices
# minDay = 0
# maxday = 1
# minDayPrice = prices[0]
# maxDayPrice = prices[1]
# currProf = maxDay - minDay 
# max_profit[i] = max{(max_profit[i-1] - prices[maxDay] + prices[i]), max_profit[i-1]} 
# maxSellAfterThisDay = [700, 700, 700, 700, 700, 700] # prices

def max_sell_day(prices):
    n = len(prices)
    maxSell = [0]*n
    maxSell[n-1] = prices[n-1]
    for i in range(n-2, 0, -1):
        maxSell[i] = max(maxSell[i+1], prices[i])
    return maxSell

'''
def DP(prices):
    n = len(prices)
    maxSell = [0]*n
    maxSell[n-1] = prices[n-1] - prices[0]
    minBuyDay = 0 
    minBuyPrice = prices[0]
    for i in range(n-2, 0, -1):
        maxSell[i] = max(maxSell[i+1], (prices[i] - prices[0])) 
    
    return maxSell
'''

def buy_day(profits):
    n = len(profits)
    maxProf = 0
    maxProfIndex = n-1 
    for i in range(n-1, -1, -1):
        if profits[i] >= maxProf:
            maxProfIndex = i
            maxProf = profits[i]
    
    if (maxProf <= 0): 
        return -1
    return maxProfIndex

def sell_day(sell_days, buy_day):
    n = len(sell_days)
    maxSell = 0
    maxSellIndex = buy_day
    for i in range(buy_day+1, n):
        if sell_days[i] >= maxSell:
            maxSell = sell_days[i]
            maxSellIndex = i

    return maxSellIndex

def DPMaxProfit(prices):
    maxSell = max_sell_day(prices)
    n = len(prices)
    profits = [0]*n
    profits[0] = max(prices[1] - prices[0], 0)
    for i in range(1, n-1):
        # print "profits[i-1]" + str(profits[i-1])
        # print "maxSell[i+1]" + str(maxSell[i+1])
        # print "prices[i]" + str(prices[i])
        profits[i] = max(profits[i-1], (maxSell[i+1] - prices[i]))
    
    day_to_buy = buy_day(profits)
    if (day_to_buy == -1):
        print("Don't buy")
    else:
        day_to_sell = sell_day(maxSell, day_to_buy)
        print("Max Profit: " + str(profits[day_to_buy]) + " when buying on day: " + str(day_to_buy) + " for: " + str(prices[day_to_buy]) + " and selling on: " + str(day_to_sell) + " for " + str(prices[day_to_sell]))

    
prices1 = [100, 150, 300, 40, 500, 700]
prices2 = [100, 55, 54, 53]
prices3 = [100, 40, 150, 700, 300, 500]
prices4 = [40, 700]
# maxSellAfterThisDay = [None, 700, 700, 700, 500, 500]

# Brute Force
'''
buy_day, sell_day, max_profit = brute_force(prices1)
         
if (buy_day is -1):
    print "Don't buy"
else: 
    print buy_day
    print sell_day
    print max_profit
'''   
DPMaxProfit(prices4)