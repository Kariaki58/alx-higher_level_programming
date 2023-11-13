#!/usr/bin/node

if (process.argv.length === 2 || isNaN(parseInt(process.argv[2], 10))) {
	console.log('Missing size');
} else {
	let number = parseInt(process.argv[2], 10);
	let squares = ""
	for (let i = 0; i < number; i++) {
		for (let j = 0; j < number; j++) {
			squares += "X"
		}
		if (i != number - 1) {
			squares += "\n"
		}
	}
	if (number > 0) {
		console.log(squares);
	}
}
