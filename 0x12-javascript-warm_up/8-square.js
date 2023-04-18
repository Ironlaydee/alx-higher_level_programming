#!/usr/bin/node
// a script that prints a square, size of the square is the first argument
// if it cannot be converted to an integer, print "Missing size"
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < size; r++) {
    let row = '';
    for (let c = 0; c < size; c++) row += 'X';
    console.log(row);
  }
}
