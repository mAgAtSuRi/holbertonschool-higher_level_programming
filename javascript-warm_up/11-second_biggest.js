#!/usr/bin/node

const { argv } = require('node:process');
let biggest = 0;
let secondBiggest = 0;
let i = 2;

while (argv[i]) {
  let number = Number(argv[i])
	if (number > biggest) {
    secondBiggest = biggest;
		biggest = number;
	} else if (number > secondBiggest) {
    secondBiggest = number;
  }
  i++;
}
console.log(secondBiggest);
