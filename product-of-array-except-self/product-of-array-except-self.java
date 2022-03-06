class Solution {
    public int[] productExceptSelf(int[] nums) {
       int len = nums.length;
        
        int[] L = new int[len];
        int[] R = new int[len];
        
        int[] answer = new int[len];
        
        L[0] = 1;
        for (int i = 1; i < nums.length; i++){
            L[i] = L[i-1] * nums[i-1];
        }
        
        R[len - 1] = 1;
        for(int j = len - 2; j >= 0 ; j--){
            R[j] = R[j+1] * nums[j+1];
        }

        for(int i = 0 ; i < len; i++){
            answer[i] = L[i] * R[i];
        }
        
        return answer;
    }
}