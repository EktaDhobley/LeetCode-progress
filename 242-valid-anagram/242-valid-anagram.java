class Solution {
    public boolean isAnagram(String s, String t) {
        
        if (s.length() != t.length())  return false;
        int count = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i = 0; i< s.length(); i++){
            char c = s.charAt(i);
            map.put(c, map.getOrDefault(c,0)+1);
        }
        
        HashMap<Character, Integer> map1 = new HashMap<>();
        for(int i = 0 ; i < t.length(); i++){
            char x = t.charAt(i);
            map1.put(x, map1.getOrDefault(x,0)+1);
            //if(map1.containsKey(x)) count++;
}
       /* if(map.containsKey(x)) count++;
      if (count == s.length() && s.length()==t.length())
        return true;
        
        else
            return false; */
        
        
        if(map.equals(map1)) return true;
        else return false;
    }
}