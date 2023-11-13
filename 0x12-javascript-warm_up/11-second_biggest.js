#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const sortArray = process.argv.slice(2, process.argv.length);
  const array = sortArray.sort((a, b) => b - a);
  const remove_dup = Array.from(new Set(array));
  console.log(remove_dup[1]);
}
