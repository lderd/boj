const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = parseInt(input[0].split(" ")[0]);
const m = parseInt(input[0].split(" ")[1]);
const tree = [];
const init = function (start, end, index) {
  if (start == end) {
    tree[index] = parseInt(input[start]);
    return tree[index];
  }
  const mid = parseInt((start + end) / 2);
  tree[index] = Math.min(
    init(start, mid, index * 2),
    init(mid + 1, end, index * 2 + 1)
  );
  return tree[index];
};
const find = function (start, end, index, left, right) {
  if (left > end || right < start) return 1000000000;
  if (left <= start && right >= end) return tree[index];
  const mid = parseInt((start + end) / 2);
  return Math.min(
    find(start, mid, index * 2, left, right),
    find(mid + 1, end, index * 2 + 1, left, right)
  );
};
init(1, n, 1);
let answer = "";
for (let i = n + 1; i < n + 1 + m; i++) {
  const s = parseInt(input[i].split(" ")[0]) - 1;
  const e = parseInt(input[i].split(" ")[1]) - 1;
  answer += find(0, n - 1, 1, s, e) + "\n";
}
console.log(answer);
