package Java;

public class Q10 {
    public int maxProfit(int[] prices) {
        /*
         * You are given an array prices where prices[i] is the price of a given stock on the ith day.
         * Find the maximum profit you can achieve. You may complete at most two transactions.
         * Note: You may not engage in multiple transactions simultaneously 
         * (i.e., you must sell the stock before you buy again).
         */
        int maxProfit = 0;
        int minPrice = Integer.MAX_VALUE;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            } else if (prices[i] - minPrice > maxProfit) {
                maxProfit = prices[i] - minPrice;
            }
        }
        return maxProfit;
    }
}
