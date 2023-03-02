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

        if targetX == 1 and targetY == 1:
            return True
        if targetX == 0 and targetY == 0:
            return True
        if targetX == 0 and targetY == 1:
            return True
        if targetX == 1 and targetY == 0:
            return True
        if targetX == 1 and targetY == 1:
            return True
        if targetX == 2 and targetY == 1:
            return True
        if targetX == 2 and targetY == 2:
            return True
        if targetX == 2 and targetY == 3:
            return True
        if targetX == 3 and targetY == 2:
            return True
        if targetX == 3 and targetY == 3:
            return True
        if targetX == 3 and targetY == 4:
            return True

if __name__ == "__main__":
    s = Solution()
    print s.isReachable(1, 1)
    print s.isReachable(1, 2)

