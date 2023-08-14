#!/usr/bin/node
function factorial (i) {
  if (isNaN(i)) {
    return (1);
  }
  if (i <= 1) {
    return (1);
  } else {
    return (i * factorial(i - 1));
  }
}
const number = parseInt(process.argv[2]);
console.log(factorial(number));
