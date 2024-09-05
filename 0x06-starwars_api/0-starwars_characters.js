#!/usr/bin/node

// A script that prints all characters of a Star Wars movie using the Star Wars API

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const film = JSON.parse(body);
  const characters = film.characters;

// Loop through each character URL and print their names
  characters.forEach(characterUrl => {
    request(characterUrl, (err, res, charBody) => {
      if (err) {
        console.error(err);
        return;
      }
      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
