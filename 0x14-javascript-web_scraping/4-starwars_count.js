#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    let movieCount = 0;
    data.results.forEach((movie) => {
      if (movie.characters.includes(characterId)) {
        movieCount++;
  }
  console.log(movieCount);
});
