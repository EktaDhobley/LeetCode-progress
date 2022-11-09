class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) #here first amt + 1 is a max default value we are giving to the array, we can give any max value also, second amt + 1 is for dp[0] ... dp[amount]
        dp[0] = 0
        
        for a in range(1,amount + 1):
            for c in coins:
                
                if a - c >= 0:
                    #that means we can compute our amount using the given coins, else for dp[2] if we have coin 5, 2-5 = -3, we cannot get 2 from coin 5.             
                    dp[a] = min(dp[a], 1 + dp[a-c]) #for c = 4, a = 6, we can say that dp[6] = 1 + dp[6-4]
                    
        return dp[amount] if dp[amount] != amount + 1 else -1
    #shouldn't be equal to our amount + 1 default value as that means we didn't find any answer, therefore return -1
                    