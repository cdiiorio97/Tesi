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

        #Approach:
        #1. Use a queue to store the points to be visited
        #2. Use a set to store the points that have been visited
        #3. Add the starting point to the queue
        #4. While the queue is not empty
        #5. Pop the first point from the queue
        #6. If the point is the target point, return true
        #7. If the point is not the target point, add the point to the set
        #8. Add the points that can be reached from the current point to the queue
        #9. Return false

        #constraints:
        #1. 1 <= targetX, targetY <= 109

        #Approach:
        #1. Use a queue to store the points to be visited
        #2. Use a set to store the points that have been visited
        #3. Add the starting point to the queue
        #4. While the queue is not empty
        #5. Pop the first point from the queue
        #6. If the point is the target point, return true
        #7. If the point is not the target point, add the point to the set
        #8. Add the points that can be reached from the current point to the queue
        #9. Return false

        #constraints:
        #1. 1 <= targetX, targetY <= 109

        #Approach:
        