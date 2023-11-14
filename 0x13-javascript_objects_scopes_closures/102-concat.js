#!/usr/bin/node

const fileStorage = require('fs');
const argv = require('process').argv;

fileStorage.readFile(argv[2], 'utf8', function (err, data) {
  if (err) {
    throw err;
  }
  fileStorage.readFile(argv[3], 'utf8', function (err, data2) {
    if (err) {
      throw err;
    }
    fileStorage.writeFile(argv[4], data + data2, err => {
      if (err) {
        throw err;
      }
    });
  });
});
