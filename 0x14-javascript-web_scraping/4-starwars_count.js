#!/usr/bin/node


const request = require("request");
const url = process.argv[2]
const character_url = "https://swapi-api.alx-tools.com/api/people/18/"


request(url, (err, respose) => {
    if (respose.statusCode == 200) {
        const body = JSON.parse(respose.body);
        const loopback = body.results;
        let count = 0;
        for (let i = 0; i < loopback.length; i++) {
            for (let j = 0; j < loopback[i].characters.length; j++) {
                if (loopback[i].characters[j] === character_url) {
                    count += 1
                }
            }
        }
        console.log(count)
    }
});
