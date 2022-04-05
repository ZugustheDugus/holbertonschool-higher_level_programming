#!/usr/bin/node
function fctrl(a) {
    if (isNaN(a)) {
        return 1;
    }
    if (a < 0) {
        return -1;
    }
    if (a === 0) {
        return 1;
    } else {
        return a * fctrl(a - 1);
    }
}
console.log(fctrl(process.argv[2]));
