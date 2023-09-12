#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('fs');
const file1 = fs.readFileSync(`./${args[0]}`);
const file2 = fs.readFileSync(`./${args[1]}`);
fs.writeFileSync(`./${args[2]}`, file1 + file2);
