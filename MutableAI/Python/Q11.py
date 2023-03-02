class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
        # The overall run time complexity should be O(log (m+n)).
        #constraints: 1 <= nums1.length <= 1000 and 1 <= nums2.length <= 1000 and -10^6 <= nums1[i], nums2[i] <= 10^6
        #nums1 and nums2 are sorted arrays.
        #Example 1:
        #nums1 = [1, 3]
        #nums2 = [2]
        #The median is 2.5, which
        #Example 2:
        #nums1 = [1, 2]
        #nums2 = [3, 4]
        #The median is (2 + 3
        #= 2.5, which

        #Solution:
        #1. merge the two arrays
        #2. find the median of the merged array
        #3. return the median
        #4. if the length of the merged array is odd, return the middle element of the
        #5. if the length of the merged array is even, return the average of the middle
        #elements of the merged array.
        #6. if the length of the merged array is even, return the average of the middle
        #elements of the merged array.

        #Example 1:
        #nums1 = [1, 3]
        #nums2 = [2]
        #The median is 2.5, which

        #Example 2:
        #nums1 = [1, 2]
        #nums2 = [3, 4]
        #The median is (2 + 3
        #= 2.5, which
        #= 2.5, which

        #Solution:
        #1. merge the two arrays

        #2. find the median of the merged array.