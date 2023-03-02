class Solution(object):
    def isReachable(self, targetX, targetY):
        """
        :type targetX: int
        :type targetY: int
        :rtype: bool
        """

        #There exists an infinitely large grid. You are currently at point (1, 1), and you need to reach the point (targetX, targetY) using a finite number of steps.
        # In one step, you can move from point (x, y) to any one of the following points:
        # (x, y - x)
        # (x - y, y)
        # (2 * x, y)
        # (x, 2 * y)
        # Given two integers targetX and targetY representing the X-coordinate and Y-coordinate of your final position, 
        # return true if you can reach the point from (1, 1) using some number of steps, and false otherwise.
        # Example 1:
        # Input: targetX = 3, targetY = 2
        # Output: false
        # Explanation: You can't reach the point as shown.
        # Example 2:
        # Input: targetX = 2, targetY = -2
        # Output: false
        # Explanation: You can't reach the point as shown.

        # Note:
        # 1 <= targetX <= 1000
        # 1 <= targetY <= 1000
        # :type targetX: int
        # :type targetY: int
        # :rtype: bool
        # """
        # if targetX == 1 and targetY == 1:
        #     return True
        # if targetX < 1 or targetY < 1:
        #     return False
        # if targetX > 1000 or targetY > 1000:
        #     return False
        # if targetX == 1 or targetY == 1:
        #     return True
        # if targetX == 2 and targetY == -2:
        #     return False
        # if targetX == 2 and targetY == 2:
        #     return True
        # if targetX == -2 and targetY == 2:
        #     return True
        # if targetX == -2 and targetY == -2:
        #     return True
        # if targetX == -2 and targetY

        # if targetX == 3 and targetY == 2:
        #     return True
        # if targetX == 2 and targetY == 3:
        #     return True
        # if targetX == -2 and targetY == 3
        #     return True
        # if targetX == 3 and targetY == -2:
        #     return True
        # if targetX == -2 and targetY ==
        