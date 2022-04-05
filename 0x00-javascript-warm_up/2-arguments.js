#!/usr/bin/node
let answer;
if (process.argv.length < 3) {
    answer = 'No argument';
} else if (process.argv.length === 3) {
    answer = 'Argument found';
} else {
    answer = 'Arguments found';
}
console.log(answer);
