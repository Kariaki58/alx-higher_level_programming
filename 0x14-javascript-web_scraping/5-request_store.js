#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const fileName = process.argv[3];
const api = process.argv[2];
const content = '';
request(api, (err, response) => {
  if (response.statusCode == 200) {
    fs.writeFile(fileName, response.body, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
