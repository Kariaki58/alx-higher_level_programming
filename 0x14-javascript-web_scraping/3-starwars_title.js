#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, (err, response) => {
  if (response.statusCode === 200) {
    const filmtitle = JSON.parse(response.body);
    console.log(filmtitle.title);
  } else {
    console.log(err);
  }
});
