const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
const T = input[0];
const cases = input.slice(1);

const MOD = 1000000009;
const maxN = Math.max(...cases);

// dp 배열 초기화
const dp = Array.from({ length: maxN + 1 }, () => [0, 0, 0]);

// 초기 값 설정
dp[1][0] = 1; // 1을 만들기 위해 마지막에 1을 사용
dp[2][1] = 1; // 2를 만들기 위해 마지막에 2를 사용
dp[3][0] = 1; // 3을 만들기 위해 마지막에 1을 사용
dp[3][1] = 1; // 3을 만들기 위해 마지막에 2를 사용
dp[3][2] = 1; // 3을 만들기 위해 마지막에 3을 사용

// dp 계산
for (let i = 4; i <= maxN; i++) {
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % MOD; // 마지막이 1
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % MOD; // 마지막이 2
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % MOD; // 마지막이 3
}

const results = cases.map(n => (dp[n][0] + dp[n][1] + dp[n][2]) % MOD);
console.log(results.join('\n'));
