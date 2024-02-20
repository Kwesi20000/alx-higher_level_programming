#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const filmsData = JSON.parse(body);
      let count = 0;
      filmsData.forEach(film => {
        if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
          count++;
        }
      });
      console.log(`Number of movies where Wedge Antilles is present: ${count}`);
    } else {
      console.error(`Failed to fetch films. Status code: ${response.statusCode}`);
    }
  }
});
