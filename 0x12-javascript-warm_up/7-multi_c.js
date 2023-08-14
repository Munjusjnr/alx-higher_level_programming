#!/usr/bin/node
const ntimes = parseInt(process.argv[2]);
if (!isNaN(ntimes)) {
  for (let i = 0; i < ntimes; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
