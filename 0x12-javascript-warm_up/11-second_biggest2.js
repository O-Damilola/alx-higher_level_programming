#!/usr/bin/node
function secondBiggest(arr){
	if (process.argv.length <= 3) {
  		console.log('0');
  	}
  	else{
  		const arr1 = process.argv.slice(2, process.argv.length).sort().reverse()
  		console.log(arr1[1]);
  	}	
}

secondBiggest(process.argv);