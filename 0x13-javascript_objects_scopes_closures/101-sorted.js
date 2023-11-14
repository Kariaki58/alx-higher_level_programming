#!/usr/bin/node

const dict = require('./101-data').dict;
const emptyDict = {};

for (const key in dict) {
  if (emptyDict[dict[key]] !== undefined) {
    emptyDict[dict[key]].push(key);
  } else {
    emptyDict[dict[key]] = [key];
  }
}

console.log(emptyDict);
