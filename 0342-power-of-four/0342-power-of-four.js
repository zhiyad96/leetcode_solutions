/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function(n) {
    let power=1;
    while(power<n){
        power*=4;

    }
    return power==n?true:false;
};