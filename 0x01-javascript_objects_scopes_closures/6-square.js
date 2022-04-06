#!/usr/bin/node
const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (chr = 'X') {
    for (let i = 0; i < this.width; i++) {
      console.log(chr.repeat(this.width));
    }
  }
};
