#!/usr/bin/node
const request = require('request');

const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(response.statusCode);
    return;
  }

  const data = JSON.parse(body);
  const title = data.title;
  console.log(title);
});
