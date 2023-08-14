#!/usr/bin/node
function secondBiggest (numlist) {
  numlist.sort((a, b) => b - a);
  return (numlist[1] || (0));
}
const argslist = process.argv.slice(2).map(arg => parseInt(arg));
console.log(secondBiggest(argslist));
