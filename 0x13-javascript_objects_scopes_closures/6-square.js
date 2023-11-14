#!/usr/bin/node

class Rectangle {
    char = "X";
    constructor (w, h) {
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
    }
    print () {
        let string = ""
        for (let i = 0; i < this.height; i++) {
            for (let j = 0; j < this.width; j++) {
                string += this.char;
            }
            if (i < this.height - 1) {
                string += "\n"
            }
        }
        console.log(string)
    }
    rotate () {
        let temp = this.width;
        this.width = this.height;
        this.height = temp;
    }
    double () {
        this.width *= 2;
        this.height *= 2;
    }
    charPrint (c) {
        if (c === undefined) {
            c = "X"
        }
        this.char = c;
        this.print();
    }
}


class Square extends Rectangle {
    constructor (size) {
        super(size, size);
    }
}

module.exports = Square;
