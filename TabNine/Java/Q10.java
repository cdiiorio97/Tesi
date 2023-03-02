package Java;

public class Q10 {
    public int maxProfit(int[] prices) {
        /*
         * You are given an array prices where prices[i] is the price of a given stock on the ith day.
         * Find the maximum profit you can achieve. You may complete at most two transactions.
         * Note: You may not engage in multiple transactions simultaneously 
         * (i.e., you must sell the stock before you buy again).
         */

         if(prices.length == 0)
            return 0;
        int min = prices[0];
        int max = 0;
        for(int i = 1; i < prices.length; i++){
            min = Math.min(min, prices[i]);
            max = Math.max(max, prices[i] - min);
        
            if(max < 0)
                max = 0;
        
                if(max < 0)
                    max = 0;
        }
        return max;
    }

}
