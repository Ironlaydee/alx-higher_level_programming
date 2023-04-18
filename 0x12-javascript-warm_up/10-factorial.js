#!/usr/bin/node
// a script that computes and prints s factorial : NaN is 1
const myArgs = process.argv.slice(2);
function factorial (num) {
  if (isNaN(myArgs[0])) {
   return 1;
  }
  if (num <= 1) {
   return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(parseInt(myArgs[0])));
