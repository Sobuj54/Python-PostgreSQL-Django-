const result = [];

for (let i = 1; i <= 50; i++) {
  if (i % 3 === 0 && i % 5 === 0) {
    result.push(i);
  }
}

console.log("Numbers divisible by both 3 and 5 from 1 to 50:", result);
