#!/usr/bin/node


const request = require("request");
const url = process.argv[2]
const character_url = "https://swapi-api.alx-tools.com/api/people/18/"


request(url, function (err, response, body) {
    if (response.statusCode == 200) {
      let Body = JSON.parse(body);
      let results = Body['results'];
      let count = 0;
      for (let i = 0; i < results.length; i++) {
        for (let j = 0; j < results[i]['characters'].length; j++) {
          if (results[i]['characters'][j] == character_url) {
            count++;
          }
        }
      }
      console.log(count);
    }
  });