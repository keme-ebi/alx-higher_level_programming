#!/usr/bin/node

function factorial (n) {
  const convert = parseInt(n);
  if (convert === 1 || isNaN(convert)) {
    return 1;
  }
  return convert * factorial(convert - 1);
}

console.log(factorial(process.argv[2]));
