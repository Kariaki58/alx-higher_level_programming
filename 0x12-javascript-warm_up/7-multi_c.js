#!/usr/bin/node

if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
} else {
  const number = parseInt(process.argv[2], 10);
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
