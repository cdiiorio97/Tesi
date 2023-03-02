package Java;
public class Q1 {
    public int removeDuplicates(int[] nums) {
        /*
         * Given an integer array nums sorted in non-decreasing order,
         * remove the duplicates in-place such that each unique element appears only once.
         * The relative order of the elements should be kept the same.
         */       
                
        int i = 0;
        int j = 1;
        int count = 0;

        while (j < nums.length) {
            if (nums[i] == nums[j]) {
                j++;
            } else {
                nums[i + 1] = nums[j];
                i++;
                j++;
                count++;
            }
        }
        return count + 1;
    }
    
}
