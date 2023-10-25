#!/usr/bin/node
const request = require('request');
const Id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${Id}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
