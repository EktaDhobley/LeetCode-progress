class Solution {
    public int minMeetingRooms(int[][] intervals) {
        if(intervals == null || intervals.length == 0) return 0;
        
        
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        int prevEndTime = intervals[0][1];
        PriorityQueue<Integer> endTimes = new PriorityQueue<>();
        endTimes.add(prevEndTime);
        for(int i = 1 ; i < intervals.length ; i++){
            int currentStart = intervals[i][0];
            int currentEnd = intervals[i][1];
            //int earliest = endTimes.remove();
            if(currentStart >= endTimes.peek()){
                endTimes.remove();
                endTimes.offer(currentEnd);
            }
            else{
                endTimes.add(currentEnd);
            }
        }
        return endTimes.size();
        
    }
}

// private static int findMinMeetingRooms(int[][] input) {
//         Arrays.sort(input, (arr1, arr2) -> Integer.compare(arr1[0], arr2[0]));
//         int previousEnd = input[0][1];
//         PriorityQueue<Integer> endtimes = new PriorityQueue<>();
//         endtimes.add(previousEnd);
//         for (int i = 1; i < input.length; i++) {
//             int currentBegin = input[i][0];
//             int currentEnd = input[i][1];
//             if (currentBegin > endtimes.peek()) {
//                 //If meeting room freed up
//                 endtimes.remove();
//                 endtimes.offer(currentEnd);
//             } else {
//                 //If no meeting rooms available
//                 endtimes.offer(currentEnd);
//             }
//         }
//         return endtimes.size();
//     }