class Solution {
   
public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        int n = strs.length;
        for(int i=0;i<n;i++){
            String s = strs[i];
            char[] arr = s.toCharArray();
            Arrays.sort(arr);
            String s2 = new String(arr);
            if(map.containsKey(s2)){
                map.get(s2).add(s);
            }
            else{
                List<String> list = new ArrayList<>();
                list.add(s);
                map.put(s2, list);
            }
        }
        
        List<List<String>> res = new ArrayList<>();
        for(String s : map.keySet()){
            List<String> list = map.get(s);
            res.add(list);
        }
        
        return res;
    
    }
}