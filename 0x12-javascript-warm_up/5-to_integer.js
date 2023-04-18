#!/usr/bin/node
// a script that prints My number: if can’t be converted to an integer, print "Not a number"
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(process.argv[2]));
