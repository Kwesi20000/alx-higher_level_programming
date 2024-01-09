#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
  // Using reduce to count occurrences
  return list.reduce((count, element) => (element === searchElement ? count + 1 : count), 0);
};
