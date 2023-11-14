#!/usr/bin/node

const RectAngle = require('./5-square');

class Square extends RectAngle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let string = '';

    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        string += c;
      }
      if (i < this.height - 1) {
        string += '\n';
      }
    }
    console.log(string);
  }
}

module.exports = Square;
