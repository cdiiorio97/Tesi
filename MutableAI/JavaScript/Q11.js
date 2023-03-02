/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    /*Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
    The overall run time complexity should be O(log (m+n)).*/
    let m = nums1.length;
    let n = nums2.length;
    let i = 0;
    let j = 0;
    let k = 0;         
    let median = 0; 
    let nums = []; 
    while (i < m && j < n) {
        if (nums1[i] < nums2[j]) {
            nums[k] = nums;
            i++;
        } else {           
            nums[k] = nums2[j];           
            j++;           
        }           
        k++;           
    }           
    while (i < m) {           
        nums[k] = nums1[i];           
        i++;           
        k++;           
    }           
    while (j < n) {           
        nums[k] = nums2[j];           
        j++;           
        k++;           
    }           
    if (k % 2) {           
        median = nums[k / 2];           
    } else {           
        median = (nums[k / 2] + nums[k / 2 - 1]) / 2;           
    }           
    return median;           
}