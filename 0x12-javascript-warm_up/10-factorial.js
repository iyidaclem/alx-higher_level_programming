#!/usr/bin/node
const num = process.argv[2];

function factorial (num) {
  if (num <= 1 || isNaN(num) || num == null) return 1;
  return num * factorial(num - 1);
}
console.log(factorial(Number(num)));
