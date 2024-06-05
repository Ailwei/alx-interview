#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-star_wars_characters.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  
  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;
  
  characterUrls.forEach(url => {
    request(url, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }
      
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
