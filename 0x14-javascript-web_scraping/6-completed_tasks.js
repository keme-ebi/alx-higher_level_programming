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
  const dict = {};

  data.forEach((task) => {
    if (task.completed) {
      const userId = task.userId;
      dict[userId] = (dict[userId] || 0) + 1;
    }
  });

  console.log(dict);
});
