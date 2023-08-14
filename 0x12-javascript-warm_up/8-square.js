#!/usr/bin/node
const sizesquare = parseInt(process.argv[2]);
if (!isNaN(sizesquare)) {
  if (sizesquare > 0) {
    for (let i = 0; i < sizesquare; i++) {
      let character = '';
      for (let s = 0; s < sizesquare; s++) {
        character += 'X';
      }
      console.log(character);
    }
  }
} else {
  console.log('Missing size');
}
