#!/usr/bin/node

function add(a, b) {
	console.log(a + b);
}

let prams1 = Number(process.argv[2]);
let prams2 = Number(process.argv[3]);

add(prams1, prams2);
