#!/usr/bin/node

function factorial(n) {
	var j = 1;
	for (i = n; i >= 1; n--){
		j = i * j;
	}
	console.log(j);
}

n = Number(process.argv[2]);
factorial(n);