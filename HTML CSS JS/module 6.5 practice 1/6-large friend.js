const friends = ["rahim", "karim", "abdul", "sadsd", "heroAlom"];

let large = friends[0];
for (const friend of friends) {
  if (friend.length >= large.length) {
    large = friend;
  }
}
console.log(large);
