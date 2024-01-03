#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const api = `https://swapi-api.alx-tools.com/api/films/${id}`;

function getCharacterName(characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (err, response) => {
      if (err) {
        reject(err);
      } else if (response.statusCode === 200) {
        const name = JSON.parse(response.body).name;
        resolve(name);
      } else {
        reject(`Failed to fetch character details for ${characterUrl}`);
      }
    });
  });
}

request(api, (err, response) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const filmData = JSON.parse(response.body);
    
    const characterPromises = filmData.characters.map(getCharacterName);

    Promise.all(characterPromises)
      .then(characterNames => {
        characterNames.forEach(name => console.log(name));
      })
      .catch(error => console.log(error));
  } else {
    console.log(`Failed to fetch film details for ID ${id}`);
  }
});
