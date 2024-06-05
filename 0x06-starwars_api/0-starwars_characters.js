#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

if (!movieId) {
  console.error('Usage: ./0-star_wars_characters.js <movie_id>');
  process.exit(1);
}

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  if (characters && characters.length > 0) {
    fetchCharacter(0, characters);
  }
});

function fetchCharacter(index, characters) {
  if (index === characters.length) {
    return;
  }

  request(characters[index], function (error, response, body) {
    if (error) {
      console.error(error);
      return;
    }

    const characterData = JSON.parse(body);
    console.log(characterData.name);
    fetchCharacter(index + 1, characters);
  });
}
