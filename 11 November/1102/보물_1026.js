function minTreasureSum(N, A, B) {

    A.sort((a, b) => a - b);
    B.sort((a, b) => b - a);
    
    let minSum = 0;

    for (let i = 0; i < N; i++) {
        minSum += A[i] * B[i];
    }
    
    return minSum;
}

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
const A = input[1].split(' ').map(Number)
const B = input[2].split(' ').map(Number)

console.log(minTreasureSum(N, A, B));