#!/usr/bin/node

const num = process.argv[2];
const convert = parseInt(num);

if (isNaN(convert)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convert);
}
