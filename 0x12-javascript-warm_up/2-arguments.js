#!/usr/bin/node
const lengt  = process.argv.length;
if (lengt  === 2) {
  console.log('No argument');
} else if (lengt  === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
