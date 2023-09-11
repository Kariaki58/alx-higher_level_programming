#!/usr/bin/node

if (process.argv.length <= 3) {
    console.log(0);
} else {
    const args = process.argv.slice(2).map(Number);
    const sortedArray = args.sort((a, b) => b - a);
    console.log(sortedArray[1]);
}
