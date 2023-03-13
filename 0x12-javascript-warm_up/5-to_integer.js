#!/usr/bin/node
if (process.argv[2] !== undefined) {
  if (isNaN(process.argv[2])) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${process.argv[2]}`);
  }
} else {
  console.log('Not a number');
}
