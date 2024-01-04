#!/usr/bin/node

const id = 18;
const url = process.argv[2];
const request = require('request');
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  for (const first of data.results) {
    for (const ch of first.characters) {
      if (ch.search(`${id}`) > 0) {
        count++;
      }
    }
  }
  console.log(count);
});
