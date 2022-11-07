class Solution:
    def isPalindrome(self, x: int) -> bool:
        #one liner solution
        #return str(x) == str(x)[::-1]
        if x < 0:
            return False
        
        newNum = 0
        inputNum = x
        while x > 0:
            newNum = newNum * 10 + x % 10 
            x = x//10
        
        return newNum == inputNum