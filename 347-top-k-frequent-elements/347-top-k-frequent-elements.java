// class Solution {
//     public int[] topKFrequent(int[] nums, int k) {
//        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
//         for(int i : nums){
//             map.put(i, map.getOrDefault(i,0)+1);
//         }
        
//         Queue<Integer> heap = new PriorityQueue(
//         (a,b) -> map.get(a) - map.get(b)
//         ); //This a custom comparator, whenever you need to order things in some custom way, you need to define a custom comparator. Comparator takes 2 inputs and returns which one is larger/smaller/equal. a-b can be +ve, 0 or -ve, which denote smaller, equal or larger.
        
//         for(int n : map.keySet()){
//             heap.add(n);
//             if( heap.size() > k) heap.poll();
//         }
        
//         int[] top = new int[k];
//         for(int i = k - 1 ; i>= 0 ; --i){
//             top[i] = heap.poll();
//         }
//         return top;
//     }
// }

class Solution{
     public int[] topKFrequent(int[] nums, int k) {
         
         HashMap<Integer, Integer> map = new HashMap<>();
         for( int i : nums){
             map.put(i , map.getOrDefault(i, 0) + 1);
         }
         
         Queue<Integer> heap = new PriorityQueue((a,b) -> map.get(a) - map.get(b));
         
         for(int n : map.keySet()){
             heap.add(n);
             if(heap.size() > k) heap.poll();
         }
         int[] top = new int[k];
         for(int i = k-1; i>= 0 ; i--){
             top[i] = heap.poll();
         }
         return top;
     }
    
}