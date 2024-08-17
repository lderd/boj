const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString().split("\n")
    : fs.readFileSync("stdin").toString().split("\r\n");

let H = Number(input[0].split(" ")[0]);
const Y = Number(input[0].split(" ")[1]);
const money = [];
money[0] = H;
for (let now = 0; now < Y; now++) {
  [
    [1, 1.05],
    [3, 1.2],
    [5, 1.35],
  ].forEach((el) => {
    const [year, mul] = el;
    if (now + year <= Y) {
      const new_money = Number.parseInt(money[now] * mul);
      if (money[now + year] > 0) {
        if (money[now + year] < new_money) {
          money[now + year] = new_money;
        }
      } else {
        money[now + year] = new_money;
      }
    }
  });
}
console.log(money[Y]);
