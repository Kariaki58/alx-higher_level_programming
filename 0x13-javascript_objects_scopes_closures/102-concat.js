#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);
const file1 = args[0];
const file2 = args[1];
const destinationFile = args[2];

fs.readFile(file1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${file1}: ${err}`);
    process.exit(1); 
  }
  fs.readFile(file2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${file2}: ${err}`);
      process.exit(1); 
    }
    const concatenatedData = data1 + data2;
    fs.writeFile(destinationFile, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${destinationFile}: ${err}`);
        process.exit(1); 
      }
      console.log(`Concatenated ${file1} and ${file2} to ${destinationFile}`);
    });
  });
});
