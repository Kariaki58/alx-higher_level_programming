#!/usr/bin/node

const dict = require("./101-data").dict
let empty_dict = {}


for (const key in dict) {
	if (empty_dict[dict[key]] !== undefined) {
		empty_dict[dict[key]].push(key)
	} else {
		empty_dict[dict[key]] = [key];
	}
}

console.log(empty_dict)
