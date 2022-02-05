class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] frequencies = new int[26];
        for (int t : tasks){
            frequencies[t - 'A']++;
        }
        Arrays.sort(frequencies);
        
        
        int maxFrequency = frequencies[25]; // cos sorted in ascending order
        int idle_time = (maxFrequency - 1) * n;
        
        for(int i = frequencies.length - 2; i >= 0 && idle_time >0 ; --i){
            idle_time = idle_time - Math.min(maxFrequency - 1, frequencies[i]);
        }
        idle_time = Math.max(0, idle_time);
        
        return idle_time + tasks.length;
    }
}