#!/usr/bin/node
exports.CallMe = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
