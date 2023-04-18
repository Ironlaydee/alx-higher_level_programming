#!/usr/bin/node
// If there is no arguments, print "No argument", if argument found print "Argument found"
// Otherwise print "Arguments Found"
 if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
