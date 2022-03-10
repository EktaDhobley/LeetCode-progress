class Solution {
    public String simplifyPath(String path) {

       Stack<String> stack = new Stack<String>();
        String[] components = path.split("/");
        
        for(String i : components){
            if(i.equals(".") || i.isEmpty()){ // kuch nai karna hai if it is a . 
                continue;
            }
            else if(i.equals("..")){ //upar wale directory mein jana hai if it is a ..
                if(!stack.isEmpty()){
                    stack.pop();
                }
            }
            else{
                stack.add(i);
            }
        }
        StringBuilder result = new StringBuilder();
        
        for(String dir : stack){
            result.append("/");
            result.append(dir);
        }
        return result.length() > 0 ? result.toString() : "/" ; 
    }
}