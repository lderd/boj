const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on("line", (line) => {
  input.push(parseInt(line));
}).on("close", () => {
  const n = input[0];
  const answer = new Set();
  for (let index = 1; index < n + 1; index++) {
    start = index;
    // 체크해야한다
    if (!answer.has(start)) {
      const check = [];
      check[start] = true;
      now = input[start];
      const tmp = [start];
      while (true) {
        // 시작점과 같다면 가능함
        if (now == start) {
          // 정답에 추가
          answer.add(...tmp);
          break;
        } else {
          // 시작점이 아닌 곳으로 도착
          if (!!check[now]) break;
          tmp.push(now);
          check[now] = true;
          now = input[now];
        }
      }
    }
  }
  const ans = [...answer];
  console.log(ans.length);
  ans.sort(function (a, b) {
    return a - b;
  });
  for (const an of ans) {
    console.log(an);
  }
  process.exit();
});
