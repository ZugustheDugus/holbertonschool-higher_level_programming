#!/usr/bin/node
const x = 'X';
const i = process.argv[2];
if (parseInt(i)) {
  for (let j = 0; j < i; j++) {
    console.log(x.repeat(i));
  }
} else {
  console.log('Missing size');
}
