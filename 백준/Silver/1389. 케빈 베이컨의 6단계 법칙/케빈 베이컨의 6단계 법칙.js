const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on("line", (line) => {
  const inputLine = line.split(" ");
  input.push(inputLine);
}).on("close", () => {
  const n = parseInt(input[0][0]);
  const m = parseInt(input[0][1]);
  const arr = [];
  arr.length = n;
  for (let i = 0; i < n; i++) {
    arr[i] = [];
    arr[i].length = n;
  }
  for (let i = 1; i < m + 1; i++) {
    const a = parseInt(input[i][0]) - 1;
    const b = parseInt(input[i][1]) - 1;
    arr[a][b] = 1;
    arr[b][a] = 1;
  }
  for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (arr[i][k] && arr[k][j]) {
          if (arr[i][j]) {
            arr[i][j] = Math.min(arr[i][j], arr[i][k] + arr[k][j]);
          } else {
            arr[i][j] = arr[i][k] + arr[k][j];
          }
        }
      }
    }
  }
  let answer = 0;
  let small = 999999999;
  for (let i = 0; i < n; i++) {
    let ssum = 0;
    for (let j = 0; j < n; j++) {
      ssum += arr[i][j];
    }
    if (ssum < small) {
      small = ssum;
      answer = i + 1;
    }
  }
  console.log(answer);
  process.exit();
});
