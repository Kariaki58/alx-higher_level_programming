#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
        return this;
      }
      this.width = w;
      this.height = h;
    }
  
    print () {
      for (let i = 0; i < this.height; i++) {
        let sqr = '';
        for (let j = 0; j < this.width; j++) {
          sqr += 'X';
        }
        console.log(sqr);
      }
    }
    rotate () {
        [this.height, this.width] = [this.width, this.height];
    }
    double () {
        this.width *= 2;
        this.height *= 2;
    }
}
module.exports = Rectangle;