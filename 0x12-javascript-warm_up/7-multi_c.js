#!/usr/bin/node
let x = +process.argv[2];
if (x){
  console.log('C is fun ' * 3);
} else {
  console.log('Missing number of occurrences');
}
