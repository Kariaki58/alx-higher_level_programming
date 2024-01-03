#!/usr/bin/node

const request = require('request');
const api = process.argv[2]

request(api, (err, reponse) => {
    if (reponse.statusCode == 200) {
        const response_body = JSON.parse(reponse.body)
        let dictionary = {}
        for (let i = 0; i < response_body.length; i++) {
            if (response_body[i].completed) {
                if (response_body[i].userId in dictionary) {
                    dictionary[response_body[i].userId] += 1
                } else {
                    dictionary[response_body[i].userId] = 1 
                }
            }
        }
        console.log(dictionary)
    }
})
