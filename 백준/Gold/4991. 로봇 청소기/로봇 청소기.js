// https://www.acmicpc.net/problem/4991

const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString().split("\n")
    : fs.readFileSync("stdin").toString().split("\r\n");

// console.log(input);
let inputIdx = 0;
let answer;
let array;
const d = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];
while (true) {
  if (input[inputIdx] === "0 0") {
    break;
  }
  const [w, h] = input[inputIdx].split(" ").map((v) => parseInt(v));
  inputIdx += 1;
  answer = 987654321;
  const present = inputIdx;
  const dirtyPlaces = {};
  let l = 1;
  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      if (input[inputIdx][j] === "o") {
        dirtyPlaces[[i, j]] = 0;
      } else if (input[inputIdx][j] === "*") {
        dirtyPlaces[[i, j]] = l;
        l += 1;
      }
    }
    inputIdx += 1;
  }
  if (l == 1) {
    console.log(0);
    continue;
  }
  // 각 더러운 곳에서 다른 모든 더러운 곳까지 거리를 저장할 배열 생성
  array = [];
  for (let i = 0; i < l; i++) {
    array[i] = new Array(l);
  }
  // 각 더러운 곳에서 다른 모든 더러운 곳까지 거리 구하기
  for (let key in dirtyPlaces) {
    // 방문확인을 할 체크배열 생성
    const checked = new Array(h);
    for (let i = 0; i < h; i++) {
      checked[i] = new Array(w);
    }
    // 첫 값(더러운 곳까지의 거리를 구할 처음 위치?)
    let [i, j] = key.split(",").map((v) => parseInt(v));
    const q = [[i, j, 0]];
    const idx = dirtyPlaces[[i, j]];
    array[idx][idx] = 0;
    // 첫 위치 방문처리
    checked[i][j] = true;
    // bfs
    while (q.length > 0) {
      const [ci, cj, cnt] = q.shift();
      for (const [di, dj] of d) {
        const ni = ci + di;
        const nj = cj + dj;
        if (
          0 <= ni &&
          ni < h &&
          0 <= nj &&
          nj < w &&
          input[present + ni][nj] !== "x" &&
          !checked[ni][nj]
        ) {
          checked[ni][nj] = true;
          if (input[present + ni][nj] !== ".") {
            array[idx][dirtyPlaces[[ni, nj]]] = cnt + 1;
          }
          q.push([ni, nj, cnt + 1]);
        }
      }
    }
  }
  for (const dist of array[0]) {
    if (dist === undefined) {
      answer = -1;
      break;
    }
  }
  if (answer > -1) {
    dfs([0], 0, l, 0);
  }
  console.log(answer);
}

function dfs(arr, idx, len, tmp) {
  if (tmp >= answer) return;
  if (idx >= len - 1) {
    if (tmp < answer) answer = tmp;
    return;
  }
  for (let i = 1; i < len; i++) {
    if (arr.includes(i)) continue;
    dfs(arr.concat(i), idx + 1, len, tmp + array[arr[idx]][i]);
  }
}
