#!/usr/bin/node
exports.converter = function (base) {
  function convertor (num) {
    return (num.toString(base));
  }
  return (convertor);
}
