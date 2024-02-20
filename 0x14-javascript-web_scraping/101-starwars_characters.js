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
      const charactersUrls = movieData.characters;
      const charactersPromises = charactersUrls.map(characterUrl => {
        return new Promise((resolve, reject) => {
          request.get(characterUrl, (charError, charResponse, charBody) => {
            if (charError) {
              reject(charError);
            } else {
              if (charResponse.statusCode === 200) {
                const characterData = JSON.parse(charBody);
                resolve(characterData.name);
              } else {
                reject(`Failed to fetch character. Status code: ${charResponse.statusCode}`);
              }
            }
          });
        });
      });

      Promise.all(charactersPromises)
        .then(names => {
          names.forEach(name => console.log(name));
        })
        .catch(error => {
          console.error(error);
        });
    } else {
      console.error(`Failed to fetch movie. Status code: ${response.statusCode}`);
    }
  }
});
