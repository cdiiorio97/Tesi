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
        
        nums = nums1 + nums2
        #sort the array
        nums.sort()
        #find the length of the array
        length = len(nums)
        #find the median
        if length % 2 == 0:
            median = (nums[length//2] + nums[length//2 - 1])/2
        else:
            median = nums[length//2]
        return median
       