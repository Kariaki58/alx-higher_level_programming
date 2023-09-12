#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newDict = {};

Object.getOwnPropertyNames(dict).forEach(data => {
  if (newDict[dict[data]] === undefined) {
    newDict[dict[data]] = [data];
  } else {
    newDict[dict[data]].push(data);
  }
});
console.log(newDict);
