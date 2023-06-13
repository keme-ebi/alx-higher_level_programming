#!/usr/bin/node

const num = process.argv[2];
const convert = parseInt(num);

if (isNaN(convert)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < convert; i++) {
    console.log('C is fun');
  }
}
