#!/usr/bin/node
/*
 * A class defining rectangle
 * The constructor must take 2 arguments w and h
 * Initialize the instance attribute width with the value of w
 * Initialize the instance attribute height with the value of h
 * create an empty object if with or height is not a real number
 */

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
