class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { '}' : '{', ']' : '[' , ')' : '(' }
        stack = []
        
        for c in s:
            #if it is a closing paranthesis(coz our keys are closing parantheses)
            if c in hashmap: 
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            else: #else if not closing paranthesis, we will just append to stack
                 stack.append(c)
        return True if not stack else False
            