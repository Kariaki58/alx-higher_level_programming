#!/usr/bin/node

let countter = 0;

exports.logMe = function count (item) {
  console.log(`${countter}: ${item}`);
  countter++;
};
