#!/usr/bin/node

function add(a, b) {
    console.log(parseInt(a) + parseInt(b));
}
args = process.argv;
add(args[2], args[3]);
