
/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";
function trim(str) {
    for (var i = 0;i<str.length;i++){
        if (str[i] != " "){
            var first_pos = i;
            // console.log(first_pos);
            break;
        }
    }
    for (var j = str.length-1;j>=0;j--){
        if (str[j] != " "){
            var last_pos = j;
            // console.log(last_pos);
            break;
        }
    }
    return str.slice(first_pos,last_pos+1);
}
console.log(trim(str1));
