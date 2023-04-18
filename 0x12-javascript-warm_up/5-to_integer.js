#!/usr/bin/node
// a script that prints My number: if can’t be converted to an integer, print "Not a number"
const num = Math.floor(Number(process.argv[2]))
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
