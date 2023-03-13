#!/usr/bin/node
let argsCount = 0;
while (process.argv[argsCount++]);
if (argsCount === 3) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
