// https://www.acmicpc.net/problem/9466

const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString().split("\n")
    : fs.readFileSync("stdin").toString().split("\r\n");

function checkVisited(now, idx) {
  if (!visited[now]) {
    visited[now] = true;
    checkVisited(input[idx][now], idx);
  } else {
    if (!cycle[now]) {
      checkCycle(now, idx);
    }
  }
  cycle[now] = true;
}

function checkCycle(now, idx) {
  if (!cycle[now]) {
    answer -= 1;
    cycle[now] = true;
    checkCycle(input[idx][now], idx);
  }
}

const T = parseInt(input[0]);
for (let t = 0; t < T; t++) {
  const n = parseInt(input[t * 2 + 1]);
  input[(t + 1) * 2] = input[(t + 1) * 2].split(" ");
  for (let i = 0; i < n; i++) {
    input[(t + 1) * 2][i] -= 1;
  }
  cycle = new Array(n);
  visited = new Array(n);
  var answer = n;
  for (let i = 0; i < n; i++) {
    checkVisited(i, (t + 1) * 2);
  }
  console.log(answer);
}
