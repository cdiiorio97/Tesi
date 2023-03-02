/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    /*Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
    The overall run time complexity should be O(log (m+n)).*/
    if(nums1.length === 0 || nums2.length === 0){
        return 0;
    }
    let m = nums1.length;
    let n = nums2.length;
    let left = 0;
    let right = m + n - 1;
    while(left <= right){
        let mid = Math.floor((left + right) / 2);
        if(nums1[mid] > nums2[mid]){
            right = mid - 1;
        }else if(nums1[mid] < nums2[mid]){
            left = mid + 1;
        }else{
            return (nums1[mid] + nums2[mid]) / 2;
        }
    }
    return 0;

    }