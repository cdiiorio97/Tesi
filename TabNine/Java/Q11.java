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
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
            m = nums1.length;
            n = nums2.length;
        }
        int i = 0;
        int j = 0;
        int k = (m + n + 1) / 2;
        while (i < m && j < n) {
            if (nums1[i] < nums2[j]) {
                nums1[k] = nums1[i];
                i++;
            } else {
                nums1[k] = nums2[j];
                j++;
            }
            k--;
        }
        while (i < m) {
            nums1[k] = nums1[i];
            i++;
            k--;
        }
        while (j < n) {
            nums1[k] = nums2[j];
            j++;
            k--;
        }
        return (m + n + 1) / 2;
    }

}
