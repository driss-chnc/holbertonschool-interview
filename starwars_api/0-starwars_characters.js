#!/usr/bin/node

const request = require('request');

function get (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error('Request failed'));
      } else {
        resolve(body);
      }
    });
  });
}

async function main () {
  const filmId = process.argv[2];
  const filmUrl = `https://swapi-api.hbtn.io/api/films/${filmId}/`;

  try {
    const filmBody = await get(filmUrl);
    const film = JSON.parse(filmBody);

    for (const characterUrl of film.characters) {
      const characterBody = await get(characterUrl);
      const character = JSON.parse(characterBody);

      console.log(character.name);
    }
  } catch (error) {

  }
}

main();
