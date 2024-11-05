const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = parseInt(input[0])
const A = input[1].split(' ').map(Number)
const M = parseInt(input[2])
const arr = input[3].split(' ').map(Number)

const binarySearch = (array, target) => {
  let left = 0
  let right = array.length - 1

  while (left <= right) {
    const mid = Math.floor((left + right) / 2)
    if (array[mid] === target) {
      return true
    } else if (array[mid] < target) {
      left = mid + 1
    } else {
      right = mid -1
    }
  }
  return false
}

A.sort((a, b) => a - b)

const result = arr.map(query => binarySearch(A, query) ? 1 : 0)

console.log(result.join('\n'))