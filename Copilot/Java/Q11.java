package Java;

public class Q11 {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        /*
         * Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
         * The overall run time complexity should be O(log (m+n)).
         */

        int n = nums1.length;
        int m = nums2.length;
        int[] nums = new int[n + m];
        int i = 0, j = 0, k = 0;

        while (i < n && j < m) {
            if (nums1[i] < nums2[j]) {
                nums[k++] = nums1[i++];
            } else {
                nums[k++] = nums2[j++];
            }
        }

        while (i < n) {
            nums[k++] = nums1[i++];
        }

        while (j < m) {
            nums[k++] = nums2[j++];
        }

        if ((n + m) % 2 == 0) {
            return (nums[(n + m) / 2] + nums[(n + m) / 2 - 1]) / 2.0;
        } else {
            return nums[(n + m) / 2];
        }

    }

}
