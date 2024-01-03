#!/usr/bin/node

const request = require('request');
const api = process.argv[2];

request(api, (err, reponse) => {
  if (reponse.statusCode === 200) {
    const responseBody = JSON.parse(reponse.body);
    const dictionary = {};
    for (let i = 0; i < responseBody.length; i++) {
      if (responseBody[i].completed) {
        if (responseBody[i].userId in dictionary) {
          dictionary[responseBody[i].userId] += 1;
        } else {
          dictionary[responseBody[i].userId] = 1;
        }
      }
    }
    console.log(dictionary);
  } else {
    console.log(err);
  }
});
