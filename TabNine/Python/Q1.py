class Q1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Given an integer array nums sorted in non-decreasing order, 
        #remove the duplicates in-place such that each unique element appears only once. 
        # The relative order of the elements should be kept the same.
        #Return the final length of the array.
        if len(nums) <= 1:
            return len(nums)
        i = 0
        j = 1
        while j < len(nums):
            if nums[i]!= nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return i + 1
    
