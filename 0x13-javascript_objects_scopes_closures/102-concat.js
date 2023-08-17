#!/usr/bin/node
const filesource = require('filesource');
const firstfile = filesource.readFileSync(process.argv[2], 'utf-8');
const secondfile = filesource.readFileSync(process.argv[3], 'utf-8');
filesource.writeFileSync(process.argv[4], firstfile + secondfile);
