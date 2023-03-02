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
    let minPrice = prices[0]
    for (let i = 1; i < prices.length; i++) {
        if (prices[i] < minPrice) {
            minPrice = prices[i]
        } else {
            maxProfit = Math.max(maxProfit, prices[i] - minPrice)
        }
    }
    return maxProfit
}