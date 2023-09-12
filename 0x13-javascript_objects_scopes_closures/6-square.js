#!/usr/bin/node

const othersquare = require('./5-square');
class Square extends othersquare {
    charPrint (c) {
        let char = c;
        if (c === undefined) {
            char = 'X';
        }
        for (let i = 0; i < this.height; i++) {
            let sqr = '';
            for (let j = 0; j < this.width; j++) {
                sqr += char;
            }
            console.log(sqr);
        }
    }
}
module.exports = Square;