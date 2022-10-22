#!/usr/bin/node
const str = 'X'
const y = Number(process.argv[2])
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} 
else {
	for (i = 0; i < y; i++) {
			console.log(str.repeat(y));
	}
}
