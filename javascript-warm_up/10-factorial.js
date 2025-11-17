#!/usr/bin/node

function factorial (a) {
  if (isNaN(a) || a <= 1) {
    return 1;
  }
  return a * factorial(a - 1);
}

const number = Number(process.argv[2]);
console.log(factorial(number));
