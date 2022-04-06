#!/usr/bin/node
const Rectangle = require('./4-rectangle');

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
