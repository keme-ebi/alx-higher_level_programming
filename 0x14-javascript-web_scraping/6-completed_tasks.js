#!/usr/bin/node

const url = process.argv[2];
const dic = {};
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  for (const dat of data) {
    if (dat.completed) {
      dic[dat.userId] = (dic[dat.userId] || 0) + 1;
    }
  }
  console.log(dic);
});
