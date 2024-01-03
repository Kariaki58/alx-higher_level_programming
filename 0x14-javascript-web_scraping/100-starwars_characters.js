#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const api = `https://swapi-api.alx-tools.com/api/films/${id}`;

function getApi (newRequest) {
  request(newRequest, (err, response) => {
    if (response.statusCode === 200) {
      const name = JSON.parse(response.body).name;
      console.log(name);
    } else {
      console.log(err);
    }
  });
}

request(api, (err, response) => {
  if (response.statusCode === 200) {
    const exactResponse = JSON.parse(response.body);
    for (let i = 0; i < exactResponse.characters.length; i++) {
      getApi(exactResponse.characters[i]);
    }
  } else {
    console.log(err);
  }
});
