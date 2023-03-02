/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    /*Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
    The overall run time complexity should be O(log (m+n)).*/

    // Merge the two arrays
    var mergedArray = nums1.concat(nums2);
    mergedArray.sort(function(a, b){return a-b});

    // Find the median
    var median = 0;
    if (mergedArray.length % 2 == 0) {
        median = (mergedArray[mergedArray.length/2] + mergedArray[(mergedArray.length/2)-1]) / 2;
    }
    else {
        median = mergedArray[Math.floor(mergedArray.length/2)];
    }

    return median;
    
};