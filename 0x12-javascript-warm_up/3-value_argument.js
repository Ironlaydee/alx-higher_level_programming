#!/usr/bin/node

// prints the first argument passed to it:
// If no arguments are passed to the script, print "No argument"
const myArgs = process.argv.slice(2);
if (!myArgs[0]) {
  console.log('No argument');
} else {
  console.log(myArgs[0]);
}
