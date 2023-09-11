#!/usr/bin/node

const array = process.argv;

if (array.length === 2) {
  console.log('Missing number of occurrences');
} else {
  const length = parseInt(array[2]);
  for (let i = 0; i < length; i++) {
    console.log('C is fun');
  }
}
