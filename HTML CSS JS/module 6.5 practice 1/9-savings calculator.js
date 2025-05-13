const monthlySavings = (arr, cost) => {
  if (!Array.isArray(arr)) return "invalid input";
  let remaining = 0;
  for (const a of arr) {
    if (a >= 3000) {
      remaining += a - a * 0.2;
    } else {
      remaining += a;
    }
  }

  if (remaining - cost >= 0) {
    return remaining - cost;
  } else {
    return "earn more";
  }
};

console.log(monthlySavings([1000, 2000, 3000], 5400));
console.log(monthlySavings([1000, 2000, 2500], 5000));
console.log(monthlySavings([900, 2700, 3400], 10000));
console.log(monthlySavings(100, [900, 2700, 3400]));
