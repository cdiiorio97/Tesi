/**
 * @param {number} targetX
 * @param {number} targetY
 * @return {boolean}
 */
var isReachable = function(targetX, targetY) {
    /*There exists an infinitely large grid. You are currently at point (1, 1), and you need to reach the point 
    (targetX, targetY) using a finite number of steps.
In one step, you can move from point (x, y) to any one of the following points:
(x, y - x)
(x - y, y)
(2 * x, y)
(x, 2 * y)
Given two integers targetX and targetY representing the X-coordinate and Y-coordinate of your final position, 
return true if you can reach the point from (1, 1) using some number of steps, and false otherwise.
    */
    if (targetX === 1 && targetY === 1) return true;
    if (targetX < 1 || targetY < 1) return false;
    if (targetX === 1 || targetY === 1) return true;
    if (targetX)
    return isReachable(targetX - 1, targetY) || isReachable;
    if (targetY) return isReachable(targetX, targetY - 1);
    return false;
}