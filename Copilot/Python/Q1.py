class Q1(object):
    def removeDuplicates(self, nums):
        #Given an integer array nums sorted in non-decreasing order, 
        #remove the duplicates in-place such that each unique element appears only once. 
        # The relative order of the elements should be kept the same.
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
        
