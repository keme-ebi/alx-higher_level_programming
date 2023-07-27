#!/usr/bin/node
const request = require('request');

const id = 18;
const url = process.argv[2];

const purl = `https://swapi-api.alx-tools.com/api/people/${id}/`;

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
  const result = data.results[1].characters[8];

  if (result === purl) {
    request(purl, (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }

      const pdata = JSON.parse(body);
      const films = pdata.films;
      const len = films.length;
      console.log(len);
    });
  }
});
