#!/usr/bin/node
const {list} = require('./100-data.js');
const newlist = list.map((value, index) => {
  return value * index});
console.log(list);
console.log(newlist);
