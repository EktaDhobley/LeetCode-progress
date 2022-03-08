class Solution {
    public int[] topKFrequent(int[] nums, int k) {
       HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i : nums){
            map.put(i, map.getOrDefault(i,0)+1);
        }
        
        Queue<Integer> heap = new PriorityQueue(
        (a,b) -> map.get(a) - map.get(b)
        );
        
        for(int n : map.keySet()){
            heap.add(n);
            if( heap.size() > k) heap.poll();
        }
        
        int[] top = new int[k];
        for(int i = k - 1 ; i>= 0 ; --i){
            top[i] = heap.poll();
        }
        return top;
    }
}