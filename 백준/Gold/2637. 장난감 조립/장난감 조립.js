const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString().split("\n")
    : fs.readFileSync("stdin").toString().split("\r\n");

// 완제품 번호
const N = input[0];
const M = Number(input[1]);
const countObject = {};
const stepSet = new Set();
for (let index = 2; index < M + 2; index++) {
  const [X, Y, K] = input[index].split(" ");
  if (!Object.hasOwn(countObject, X)) {
    countObject[X] = {};
  }
  stepSet.add(X);
  countObject[X][Y] = Number(K);
}
const defaultCountObject = {};
Object.keys(find(N)).forEach((e) => console.log(e, defaultCountObject[N][e]));

function find(x) {
  // 계산한 적이 없다면 부품별 수량 계산
  if (!Object.hasOwn(defaultCountObject, x)) {
    // 중간 부품이 아니라면(기본 부품이라면)
    if (!stepSet.has(x)) {
      defaultCountObject[x] = {};
      defaultCountObject[x][x] = 1;
      return defaultCountObject[x];
    }
    defaultCountObject[x] = {};
    // element => 필요한 부품 명
    // countObject[element] => 필요한 부품의 필요한 부품별 수량
    Object.keys(countObject[x]).forEach((element) => {
      // find(element) => 필요한 부품을 만드는데 필요한 기본부품 별 수량 object
      // el => 필요한 부품을 만드는데 필요한 기본부품
      Object.keys(find(element)).forEach((el) => {
        if (!Object.hasOwn(defaultCountObject[x], el)) {
          defaultCountObject[x][el] = 0;
        }
        defaultCountObject[x][el] +=
          countObject[x][element] * defaultCountObject[element][el];
      });
    });
  }
  // 부품별 수량 반환
  return defaultCountObject[x];
}
