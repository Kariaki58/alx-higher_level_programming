#!/usr/bin/node

function Factorial (value) {
    if (isNaN(parseInt(value)) || value === 1) {
        return (1);
    }
    return (value * Factorial(value - 1));
}

console.log(Factorial(parseInt(process.argv[2])));
