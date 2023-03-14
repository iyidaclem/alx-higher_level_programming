#!/usr/bin/node
const SquareP = require('./5-square.js');

class Square extends SquareP {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const _str = c !== undefined ? c : 'X';
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) str += _str;
      console.log(str);
    }
  }
}

module.exports = Square;
