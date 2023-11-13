#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const prams1 = Number(process.argv[2]);
const prams2 = Number(process.argv[3]);

add(prams1, prams2);
