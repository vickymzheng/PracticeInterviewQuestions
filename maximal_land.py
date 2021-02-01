# Jeff Flake
#  I want buy land, and all of the land is at different prices. 
# I want to maximum contiguous amount of land I can get within a certain budget. 
# Each of the plots of land is a different price, but all plots of land are the same size. 
# A contiguous block of land corresponds to a contiguous segment in the price array. 

def get_maximal_land_size(prices, budget):
	starting = 0
	for i, price in enumerate(prices):
		starting = i
		if price < budget:
			break 

	n = len(prices)
	if (starting == n-1):
		return 0

	max_cont_block_size = curr_block_size = 1
	curr_block_start = starting
	curr_block_cost = prices[starting]
	starting+=1

	for i in range(starting, n):
		land_cost = prices[i]

		while ( (land_cost + curr_block_cost > budget) and (curr_block_start < i) ):
			curr_block_cost-=prices[curr_block_start]
			curr_block_size-=1 
			curr_block_start+=1 
		if not (land_cost + curr_block_cost > budget):
			curr_block_cost += land_cost
			curr_block_size += 1
			if (curr_block_size > max_cont_block_size):
				max_cont_block_size = curr_block_size
	
	return max_cont_block_size

print(get_maximal_land_size([6], 5))
