#!/usr/bin/node


const request = require("request");
const url = process.argv[2]
const character_url = "https://swapi-api.alx-tools.com/api/people/18/"


request(url, (err, respose) => {
    if (respose.statusCode == 200) {
        const body = JSON.parse(respose.body);
        const loopback = body.results;
        const wedgeMovies = loopback.filter(film => 
            film.characters.includes(character_url)
        );
        console.log(wedgeMovies.length);
    }
});
