#!/usr/bin/node
exports.esrever = function (list) {
  const listreversed = [];

  for (let x = list.length - 1; x >= 0; x--) {
    listreversed.push(list[x]);
  }
  return (listreversed);
};
