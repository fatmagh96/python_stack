/* 
    Acronyms

    Create a function that, given a string, returns the string’s acronym 
    (first letter of each word capitalized). 

    Do it with .split first if you need to, then try to do it without
*/

const str1 = "object oriented programming";
const expected1 = "OOP";

// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expected2 = "APIE";

const str3 = "software development life cycle";
const expected3 = "SDLC";

// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expected4 = "GIT";

function acronymize(str) {
    var arr = str.split(' ');
    // console.log(arr);
    var acronym = '';
    for (let i = 0; i < arr.length; i++) {
        // console.log(arr[i][0].toUpperCase());
        if (arr[i].length > 0) {
            acronym += arr[i][0].toUpperCase();
        }
    }
    return acronym;
}

console.log(acronymize(str1));

console.log(acronymize(str2));

console.log(acronymize(str3));

console.log(acronymize(str4));



// Without Split //

function acronymizeWithoutSplit(str) {
    var result = "";
    if (str[0] != " ") {
        result += str[0].toUpperCase();
    }
    for (var i = 0; i < str.length - 2; i++) {
        if (str[i] == " " && str[i+1] != 0) {
            result += str[i+1].toUpperCase();
        }
    }
    return result;
}


console.log(acronymizeWithoutSplit(str1));

console.log(acronymizeWithoutSplit(str2));

console.log(acronymizeWithoutSplit(str3));

console.log(acronymizeWithoutSplit(str4));