class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        
        for i, v1 in enumerate(transactions):
            name1, time1, amount1, city1 = v1.split(',')
            
            if int(amount1) > 1000:
                invalid.append(v1)
                continue
                
            for j, v2 in enumerate(transactions):
                if i != j:
                    name2, time2, amount2, city2 = v2.split(',')
                    if name1 == name2 and abs(int(time2) - int(time1)) <= 60 and city1 != city2:
                        invalid.append(v1)
                        break
                        
        return invalid