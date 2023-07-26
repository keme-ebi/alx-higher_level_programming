#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];

const file = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(response.statusCode);
    return;
  }

  fs.writeFile(file, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
