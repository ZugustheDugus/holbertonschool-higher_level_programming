#!/usr/bin/node
const string = 'C is fun';
let x = process.argv[2];
if (parseInt(x)) {
  while (x > 0) {
    console.log(string);
    x--;
  }
} else {
  console.log('Missing number of occurrences');
}
