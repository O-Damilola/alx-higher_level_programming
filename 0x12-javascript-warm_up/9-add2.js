#!/usr/bin/node
function add(a, b) {
	console.log(Number(a) + Number(b))
}

a = process.argv[2]
b = process.argv[3]
add(a, b)