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

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        elif len(nums1) < len(nums2):
            return self.findMedianSortedArrays(nums1, nums2)
        else:
            if len(nums1) % 2 == 1:
                return (nums1[len(nums1) // 2] + nums2[len(nums2) // 2]) / 2.0
            else:
                return (nums1[len(nums1) // 2] + nums2[len(nums2) // 2]) / 2.0
            
    