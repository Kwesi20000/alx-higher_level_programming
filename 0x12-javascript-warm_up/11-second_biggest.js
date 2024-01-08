#!/usr/bin/node

function findSecondBiggest(args) {
  const integers = args.map(arg => parseInt(arg)).filter(num => !isNaN(num));
  const uniqueIntegers = Array.from(new Set(integers)); // Remove duplicates

  if (uniqueIntegers.length < 2) {
    return 0;
  }

  const sortedIntegers = uniqueIntegers.sort((a, b) => b - a);
  return sortedIntegers[1];
}

const args = process.argv.slice(2);
const secondBiggest = findSecondBiggest(args);
console.log(secondBiggest);
