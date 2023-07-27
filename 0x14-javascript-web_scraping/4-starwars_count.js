#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

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

  request(result, (err, response, body) => {
    if (err) {
      console.error(err);
      return;
    }

    const pdata = JSON.parse(body);
    const films = pdata.films;
    const len = films.length;
    console.log(len);
  });
});
