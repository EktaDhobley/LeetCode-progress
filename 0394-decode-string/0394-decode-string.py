class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)): 
            if s[i] != ']':
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != '[':
                    substr = stack.pop() + substr #imp not to do substr+=
                stack.pop()  #to remove the '['
            
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k #imp not to do k+=
                stack.append(int(k) * substr)
            
        return "".join(stack)
        