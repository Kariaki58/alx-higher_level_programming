#!/usr/bin/node

const list = require('./100-data.js').list;

const mewarray = list.map((val, index) => val * index);
console.log(list);
console.log(mewarray);