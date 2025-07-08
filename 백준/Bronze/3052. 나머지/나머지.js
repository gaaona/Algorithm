const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const remainders = new Set();

for (let i = 0; i < 10; i++) {
    const num = parseInt(input[i]);
    remainders.add(num % 42);
}

console.log(remainders.size);