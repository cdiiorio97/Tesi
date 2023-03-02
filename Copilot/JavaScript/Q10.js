/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    /*You are given an array prices where prices[i] is the price of a given stock on the ith day.
    Find the maximum profit you can achieve. You may complete at most two transactions.
    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
    */
    let maxProfit = 0;
    let minPrice = prices[0];
    let maxPrice = prices[0];
    let maxProfit1 = 0;
    let maxProfit2 = 0;
    for (let i = 1; i < prices.length; i++) {
        if (prices[i] < minPrice) {
            minPrice = prices[i];
            maxPrice = prices[i];
        }
        if (prices[i] > maxPrice) {
            maxPrice = prices[i];
        }
        maxProfit1 = Math.max(maxProfit1, maxPrice - minPrice);
    }
    maxProfit += maxProfit1;
    minPrice = prices[prices.length - 1];
    maxPrice = prices[prices.length - 1];
    for (let i = prices.length - 2; i >= 0; i--) {
        if (prices[i] > maxPrice) {
            maxPrice = prices[i];
            minPrice = prices[i];
        }
        if (prices[i] < minPrice) {
            minPrice = prices[i];
        }
        maxProfit2 = Math.max(maxProfit2, maxPrice - minPrice);
    }
    maxProfit += maxProfit2;
    return maxProfit;
    
};