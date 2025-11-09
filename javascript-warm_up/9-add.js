#!/usr/bin/node

function add(a, b) {
  firstArg = process.argv[2];
  secondArg = process.argv[3];
  console.log(`${firstArg + secondArg}`);
}
