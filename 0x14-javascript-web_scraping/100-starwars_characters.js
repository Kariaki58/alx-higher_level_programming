#!/usr/bin/node

const request = require('request');
const id = process.argv[2]
const api = `https://swapi-api.alx-tools.com/api/films/${id}`


function getApi(newRequest) {
    request(newRequest, (err, response) => {
        const name = JSON.parse(response.body)['name']
        console.log(name)
    })
}

request(api, (err, response) => {
    const exact_response = JSON.parse(response.body)
    for (let i = 0; i < exact_response['characters'].length; i++) {
        getApi(exact_response['characters'][i])
    }
});
