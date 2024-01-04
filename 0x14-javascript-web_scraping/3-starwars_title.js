#!/usr/bin/node

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const movie = JSON.parse(body);
  console.log(`${movie.title}`);
});
