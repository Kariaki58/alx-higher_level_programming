#!/usr/bin/node

const dict = require("./101-data").dict
let empty_dict = {}


for (const key in dict) {
	if (dict[key] in Object.keys(empty_dict)) {
		empty_dict[dict[key]].push(key)
	} else {
		empty_dict[dict[key]] = [];
		empty_dict[dict[key]].push(key)
	}
}

console.log(empty_dict)
