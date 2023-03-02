package Java;

public class Q12 {
    public boolean isReachable(int targetX, int targetY) {
        /*There exists an infinitely large grid. You are currently at point (1, 1), and you need to reach the point 
        (targetX, targetY) using a finite number of steps.
        In one step, you can move from point (x, y) to any one of the following points:
        (x, y - x)
        (x - y, y)
        (2 * x, y)
        (x, 2 * y)
        Given two integers targetX and targetY representing the X-coordinate and Y-coordinate of your final position, 
        return true if you can reach the point from (1, 1) using some number of steps, and false otherwise. */
      
        int x = 1;
        int y = 1;
        int steps = 0;
        while (x != targetX || y != targetY) {
            if (x == targetX && y == targetY) {
                return true;
            } else if (x == targetX) {
                y++;
            } else if (y == targetY) {
                x++;
            } else if (x > targetX && y > targetY) {
                x--;
                y--;
            } else if (x > targetX) {
                x--;
            } else if (y > targetY) {
                y--;
            } else if (x < targetX && y < targetY) {
                x++;
                y++;
            } else if (x < targetX) {
                x++;
            } else if (y < targetY) {
                y++;
            } else {
                return false;
            }
            steps++;
        }
        return true;
    }
}
