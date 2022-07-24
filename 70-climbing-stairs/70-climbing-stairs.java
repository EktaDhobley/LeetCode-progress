public class Solution {
    
     int[] memo;
    public int climbStairs(int n) {
        memo = new int[n+1];
        
        return helper(n);
    }
    
    public int helper(int n){
        if(n==0){
            return 1;
        }
        if(n<0){
            return 0;
        }
        if(memo[n]!=0)
            return memo[n];
        
        memo[n] = helper(n-1)+helper(n-2);
        
        return memo[n];
    }

}






// public class Solution {
//     public int climbStairs(int n) {
//         if( n == 1 ){
//             return 1;
//         }
//         int dp[] = new int[n+1];
//         dp[1]= 1;
//         dp[2]= 2;
        
//         for(int i = 3; i <=n ; i++){
//             dp[i] = dp[i-1] + dp[i-2];
//         }
//         return dp[n];
//     }
// }
        