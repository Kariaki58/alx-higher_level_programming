#!/usr/bin/node

let args = process.argv.slice(2);
let fs = require('fs');
let file1 = fs.readFileSync(`./${args[0]}`);
let file2 = fs.readFileSync(`./${args[1]}`);
fs.writeFileSync(`./${args[2]}`, file1 + file2);