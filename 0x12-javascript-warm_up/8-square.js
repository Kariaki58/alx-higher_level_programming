#!/usr/bin/node

const array = process.argv;

if (array.length === 2 || isNaN(array[2])) {
  console.log('Missing size');
}
for (let i = 0; i < parseInt(array[2]); i++) {
  let string = '';
  for (let j = 0; j < parseInt(array[2]); j++) {
    string += 'X';
  }
  console.log(string);
}
