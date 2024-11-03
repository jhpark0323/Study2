const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const K = parseInt(input[0])
const stack = []

for (let i = 1; i <= K; i++) {
  const number = parseInt(input[i])

  if (number === 0) {
    stack.pop()
  } else {
    stack.push(number)
  }
}

const result = stack.reduce((acc, num) => acc + num, 0)
console.log(result)