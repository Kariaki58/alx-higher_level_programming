#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const sortArray = process.argv.slice(2, process.argv.length);
  const array = sortArray.sort((a, b) => b - a);
  const removeDup = Array.from(new Set(array));
  console.log(removeDup[1]);
}
