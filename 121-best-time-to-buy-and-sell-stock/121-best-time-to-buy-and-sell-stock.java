class Solution {
    public int maxProfit(int[] prices) {
        // //intialize day-1 values i.e profit is zero just now we buy and that is the min value
        // int min = prices[0], profit = 0, N =prices.length;
        // for(int i=1; i<N; i++){
        //     min = Math.min(min, prices[i]);         //keep track of min value
        //     profit = Math.max(profit, prices[i]-min); //calculate profit on the next days of min value
        // }
        // return profit;
        
        int maxProf = 0;
        int min = Integer.MAX_VALUE;
        
        for(int i = 0 ; i < prices.length ; i++){
            if( prices[i] < min ){
                min = prices[i];
            }
            else{
                maxProf = Math.max(maxProf, prices[i] - min);
            }
        }
        return maxProf;
    }
}