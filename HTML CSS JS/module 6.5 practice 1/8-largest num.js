var numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10];

let large = numbers[0];

for (const num of numbers) {
  if (num >= large) large = num;
}
console.log("largest: ", large);
