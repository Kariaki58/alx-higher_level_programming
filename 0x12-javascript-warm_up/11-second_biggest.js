#!/usr/bin/node

if (process.argv.length < 4) {
	console.log(0);
} else {
	let sortArray = process.argv.slice(2);
	console.log(parseInt(sortArray.sort()[sortArray.length - 2], 10));
}
