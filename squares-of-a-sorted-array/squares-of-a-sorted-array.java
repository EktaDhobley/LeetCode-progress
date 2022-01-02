class Solution {
    public int[] sortedSquares(int[] A) {
        int[] nums = new int[A.length];
        int k=A.length-1;
        int i=0, j=A.length-1;
        while(i<=j){
            if(Math.abs(A[i]) <= Math.abs(A[j])){
                nums[k--] = A[j]*A[j];
                j--;
            }
            else{
                nums[k--] = A[i]*A[i];
                i++;
            }    
        }
        return nums;
    }
}