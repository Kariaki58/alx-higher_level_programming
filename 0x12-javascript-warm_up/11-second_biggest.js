#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const sortArray = process.argv.slice(2);
  const array = sortArray.sort();
  for (let i = 0; i < array.length; i++) {
    if (i < array.length - 1) {
      if (array[i] === array[i + 1]) {
        array.pop();
      }
    }
  }
  console.log(array);
  console.log(array[array.length - 2]);
}
