#!/usr/bin/node

const arg = process.argv[2];
const numberOfOccurrences = parseInt(arg);

if (isNaN(numberOfOccurrences)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numberOfOccurrences; i++) {
    console.log('C is fun');
  }
}
