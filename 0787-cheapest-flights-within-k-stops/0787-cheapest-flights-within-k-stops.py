class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float("inf")] * n
        prices[src] = 0
        
        for i in range(k + 1):
            tmpPrices = prices.copy()
            for s, d, p in flights: #source, destination, price
                if prices[s] == float("inf"): #if we cant reach the source node #except the first src given in question where prices[src] = 0
                    continue
                if prices[s] + p < tmpPrices[d]: #if we reach source node, and the price to reach node (d) after that is price to reach source node + price to reach the node (d) after source node , and if it is less than the tmpPrice[d] then we substitute it with the lower value
                    tmpPrices[d] = prices[s] + p
                    
            prices = tmpPrices
                    
        
        return -1 if prices[dst] == float("inf") else prices[dst]
        