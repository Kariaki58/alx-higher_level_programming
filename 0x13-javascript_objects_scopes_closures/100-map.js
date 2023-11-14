#!/usr/bin/node

const list = require('./100-data').list;
const secondList = list.map((val, ind) => val * ind);

console.log(list);
console.log(secondList);
