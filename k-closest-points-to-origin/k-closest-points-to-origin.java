class Solution {
    public int[][] kClosest(int[][] points, int k) {
        
      
       PriorityQueue<int[]> pq = new PriorityQueue<>(
       (a, b) -> ((a[0] * a[0]) + ( a[1] * a[1]) - (b[0] * b[0]) - (b[1]*b[1])) 
       ); //Once the heap is "full", we can then compare each new point to the farthest point stored in the heap. If the new point is closer, then we should remove the farthest point from the heap and insert the new point.  
        
     for(int i = 0 ; i<points.length; i++){
         pq.add(new int[]{points[i][0] , points[i][1]});
         //System.out.println(pq);
     }
        
        int res[][] = new int[k][2];
        for( int i = 0 ; i< k && !pq.isEmpty() ; i++){
            res[i] = pq.poll();
        }
        
        return res;
    }
}