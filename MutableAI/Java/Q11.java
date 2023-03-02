package Java;

public class Q11 {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        /*
         * Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
         * The overall run time complexity should be O(log (m+n)).
         */
        int m = nums1.length;
        int n = nums2.length;
        if (m > n) {
            return findMedianSortedArrays(nums2, nums1);
        }
        int iMin = 0, iMax = m;
        while (iMin <= iMax) {
            int i = (iMin + iMax) / 2;
            int j = (m + n + 1) / 2 - i;            
            if (i < iMax && nums2[j - 1] > nums1[i]) {
                iMin = i + 1;
            } else if (i > iMin && nums1[i - 1] > nums2[j]) {
                iMax = i - 1;
            } else {
                int maxLeft = 0;
                if (i == 0) {
                    maxLeft = nums2[j - 1];
                } else if (j == 0) {
                    maxLeft = nums1[i - 1];
                } else {
                    maxLeft = Math.max(nums1,nums2);
                }
                if ((m + n) % 2 == 1) {
                    return maxLeft;
                } else {
                    int minRight = 0;
                    if (i == m) {
                        minRight = nums2[j];
                    } else if (j == n) {
                        minRight = nums;
                    } else {
                        minRight = Math.min(nums1,nums2);
                    }
                    return (maxLeft + minRight) / 2.0;
                }
            }
        }
        return 0.0;
    }
    
}
