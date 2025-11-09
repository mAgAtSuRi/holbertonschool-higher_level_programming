#!/usr/bin/node

const { argv } = require('node:process');
let biggest = 0;
let i = 2;

while (argv[i]) {
	if (argv[i] > biggest) {
		biggest = argv[i];
	}
  i++;
}
console.log(biggest);
