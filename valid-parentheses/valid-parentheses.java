
/*
class Solution{
    public boolean isValid(String s){
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> map = new HashMap<>();
        map.put('{','}');
        map.put('[',']');
        map.put('(',')');
        
        for(Character c : s.toCharArray()){
            if(!stack.isEmpty() && map.get(stack.peek()) == c){
                stack.pop();
            }
            else {
                stack.push(c);
            }
        }
        return stack.isEmpty();
        
    }
}
*/

class Solution{
    public boolean isValid(String s){
        
        Stack<Character> stack = new Stack<>();
        
        HashMap<Character, Character> map = new HashMap<>();
        map.put('{','}');
        map.put('[',']');
        map.put('(',')');
        
        
        for(Character c : s.toCharArray()){
            if(!stack.isEmpty() && map.get(stack.peek()) == c){
                stack.pop();
            }
            else{
                stack.push(c);
            }
        }
        
        
        
        
        return stack.isEmpty();
        
        
        
        
        
        
        
        
        
        
        
    }
}
