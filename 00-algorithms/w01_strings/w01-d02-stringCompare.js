/**
 * Determines whether or not the strings are equal, ignoring case.
 * @param {string} strA
 * @param {string} strB
 * @returns {boolean} If the strings are equal or not.
 */

var strA1 = "ABC";
var strB1 = "abc";
var expected1 = true;

var strA2 = "ABC";
var strB2 = "abd";
var expected2 = false;

var strA3 = "ABC";
var strB3 = "bc";
var expected3 = false;

// ! BONUS 

var strA4 = "Dad ";
var strB4 = " dAd";
var expected4 = true;

function caseInsensitiveStringCompare(strA, strB) {
    // compare strings 
    if (strA.trim().toUpperCase() == strB.trim().toUpperCase()){
        return true;
    }
    else return false;
}
console.log(caseInsensitiveStringCompare(strA1, strB1))
console.log(caseInsensitiveStringCompare(strA2, strB2))
console.log(caseInsensitiveStringCompare(strA3, strB3))
console.log(caseInsensitiveStringCompare(strA4, strB4))

