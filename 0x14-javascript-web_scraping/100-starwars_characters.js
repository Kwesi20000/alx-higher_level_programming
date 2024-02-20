#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      console.log(`Characters in ${movieData.title}:`);
      movieData.characters.forEach(characterUrl => {
        request.get(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError);
          } else {
            if (charResponse.statusCode === 200) {
              const characterData = JSON.parse(charBody);
              console.log(characterData.name);
            } else {
              console.error(`Failed to fetch character. Status code: ${charResponse.statusCode}`);
            }
          }
        });
      });
    } else {
      console.error(`Failed to fetch movie. Status code: ${response.statusCode}`);
    }
  }
});
