#!/usr/bin/node
// A class defining square that inherits from a mother square

const MotherSquare = require('./5-square.js');
class Square extends MotherSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
