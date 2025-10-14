/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let pali=parseInt(x.toString().split("").reverse().join(""))
    return x===pali;
};
console.log(121);