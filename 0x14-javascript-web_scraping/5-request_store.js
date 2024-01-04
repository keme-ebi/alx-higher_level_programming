#!/usr/bin/node

const url = process.argv[2];
const file = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
