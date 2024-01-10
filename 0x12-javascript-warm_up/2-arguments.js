#!/usr/bin/node
const process = require('node:process');
if (process.argv.length === 2) {
  console.log('No arguments found');
} else {
  console.log('Arguments found');
}
