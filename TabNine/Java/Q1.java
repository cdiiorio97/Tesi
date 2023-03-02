package Java;

public class Q1 {
    public int removeDuplicates(int[] nums) {
        /*
         * Given an integer array nums sorted in non-decreasing order,
         * remove the duplicates in-place such that each unique element appears only once.
         * The relative order of the elements should be kept the same.
         */
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[j]!= nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    
        
}
}
