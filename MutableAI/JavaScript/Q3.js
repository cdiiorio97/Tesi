/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function(n) {
    //Reverse bits of a given 32 bits unsigned integer.
    
    let result = 0; 
    for (let i = 0; i < 32; i++) {
        result = result << 1;
        result = result | (n & 1);
        n = n >> 1;
    }
    return result;
}
