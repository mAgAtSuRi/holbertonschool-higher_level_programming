#!/usr/bin/node
const { argv } = require('node:process')
for (i = 2; i < 5; i++) {
  console.log(`${argv[i]}`);
}
