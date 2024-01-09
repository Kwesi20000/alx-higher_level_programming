#!/usr/bin/node
module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    } else {
      // Return an empty object if conditions are not met
      return Object.create(null);
    }
  }
};
