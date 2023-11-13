#!/usr/bin/node

function factorial(n) {
	if (n === 1) {
		return (1);
	}
	return n * factorial(n - 1);
}

if (isNaN(parseInt(Number(process.argv[2]), 10))) {
	console.log(1);
} else {
	console.log(factorial(parseInt(Number(process.argv[2], 10))));
}
