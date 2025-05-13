var numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10];

const unique = [];

for (const num of numbers) {
  if (!unique.includes(num)) {
    unique.push(num);
  }
}

console.log(unique);
