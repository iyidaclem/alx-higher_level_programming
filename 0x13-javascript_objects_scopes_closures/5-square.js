#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

module.exports = class Sqaure extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
