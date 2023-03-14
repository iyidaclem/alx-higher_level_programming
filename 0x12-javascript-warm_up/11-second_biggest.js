#!/usr/bin/node
const args = process.argv;

function secondBiggest (x) {
  let big = 0;
  let bigger = 0;
  for (let i = 2; i < x.length; i++) {
    if (Number(x[i]) > bigger) {
      big = bigger;
      bigger = Number(x[i]);
    } else if (Number(x[i]) > big) big = Number(x[i]);
  }
  return big;
}

if (args.length < 4) {
  console.log(0);
} else {
  console.log(secondBiggest(args));
}
