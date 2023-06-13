#!/usr/bin/node

const num = process.argv[2];
const convert = parseInt(num);

if (isNaN(convert)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < convert; i++) {
    let row = '';
    for (let j = 0; j < convert; j++) {
     row += 'X';
    }
    console.log(row);
  }
}
