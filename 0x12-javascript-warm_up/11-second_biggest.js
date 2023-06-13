#!/usr/bin/node

function secondLargest (numbers) {
  const sorted = numbers.sort((a, b) => b - a);
  return sorted[1];
}

const cmdarg = process.argv.slice(2);
const args = cmdarg.map(arg => Number(arg));
if (process.argv.length < 3 || process.argv.length < 4) {
  console.log(0);
} else {
  console.log(secondLargest(args));
}
