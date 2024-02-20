#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
          console.error(err);
        } else {
          console.log(`Webpage content has been saved to ${filePath}`);
        }
      });
    } else {
      console.error(`Failed to fetch webpage. Status code: ${response.statusCode}`);
    }
  }
});
