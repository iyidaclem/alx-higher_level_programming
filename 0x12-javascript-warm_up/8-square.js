#!/usr/bin/node
if (isNaN(process.argv[2]) || (process.argv[2] === undefined)) {
  console.log('Missing size');
} else {
  for (let i = process.argv[2]; i > 0; i--) {
    let str = '';
    for (let j = 0; j < process.argv[2]; j++) str += 'X';
    console.log(str);
  }
}
