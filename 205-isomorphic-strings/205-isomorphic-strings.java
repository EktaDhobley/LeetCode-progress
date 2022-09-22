// class Solution {
//     public boolean isIsomorphic(String s, String t) {
        
//         HashMap<Character, Character> map = new HashMap<>();
        
//         for(int i = 0; i < s.length(); i++){
//             if(!map.containsKey(s.charAt(i))){
//                 map.put(s.charAt(i), t.charAt(i));
//             }
//             else{
//                 if(t.charAt(i) != map.get(s.charAt(i)))
//                 return false;
//             }
            
//         }
//         //To check if there are any duplicates in values of map
//         List<Character> list = new ArrayList<>(map.values());
//         Set<Character> set = new HashSet<>(list);
//         if(list.size() != set.size()){
//             return false;
//         }
//         return true;
//     }
// }

//#2 - Better Solution
// class Solution {
//     public boolean isIsomorphic(String s, String t) {
//         HashMap<Character, Character> map = new HashMap<>();
//         for (int i = 0; i < s.length(); i++) {
//             if (map.containsKey(s.charAt(i))) {
//                 if (t.charAt(i) != map.get(s.charAt(i)))
//                     return false;
//             } else {
//                 if (map.containsValue(t.charAt(i)))
//                     return false;
//                 map.put(s.charAt(i), t.charAt(i));
//             }
//         }
//         return true;
//     }
// }













class Solution {
    public boolean isIsomorphic(String s, String t) {
     HashMap<Character, Character> map = new HashMap<>();
     for(int i = 0; i < s.length(); i++){
         if(!map.containsKey(s.charAt(i))){
             map.put(s.charAt(i), t.charAt(i));
         }
         else{
             if(t.charAt(i) != map.get(s.charAt(i)))
                 return false;
         }
     }
        List<Character> list = new ArrayList<>(map.values());
        Set<Character> set = new HashSet<>(list);
        if(list.size() != set.size()) return false;
        return true;
    }
    
}
