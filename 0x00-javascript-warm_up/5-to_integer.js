#!/usr/bin/node
const intj = parseInt(process.argv[2]);
if (intj) {
  console.log('My number: ' + intj);
} else {
  console.log('Not a number');
}
