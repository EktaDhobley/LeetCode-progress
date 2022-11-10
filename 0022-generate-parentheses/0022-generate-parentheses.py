class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open paratheses if open < n
        #only add a closing paranthesis if closed < open
        #valid IIF open == close == n
        
        
        res = []
        
        def backtrack(stack, left, right):
            if left == right == n:
                res.append("".join(stack))
                return
            if left < n:
                #stack.append("(")
                backtrack(stack + ["("], left + 1, right)
                #stack.pop()
            if right < left:
                #stack.append(")")
                backtrack(stack + [")"], left, right + 1)
                #stack.pop()
        backtrack([], 0, 0)
        return res
                
                