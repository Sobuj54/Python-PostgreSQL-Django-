const box = document.getElementsByClassName("box");

for (let i = 0; i < box.length; i++) {
  const element = box[i];
  if (element.innerText == "box-4") {
    element.style.backgroundColor = "green";
  } else element.style.backgroundColor = "yellow";
}

// document.getElementById("btn").addEventListener("click", () => {
// const inputVal = document.getElementById("input-field").value;
// const container = document.getElementById("container");
// const p = document.createElement("p");
// p.innerText = inputVal;
// container.appendChild(p);
// document.getElementById("input-field").value = " ";
// });

// another way
const handleAdd = () => {
  const inputVal = document.getElementById("input-field").value;
  const container = document.getElementById("container");
  const p = document.createElement("p");
  p.classList.add("child");
  p.innerText = inputVal;
  container.appendChild(p);
  document.getElementById("input-field").value = " ";

  // remove added elements
  const allChild = document.getElementsByClassName("child");

  for (child of allChild) {
    child.addEventListener("click", (e) => {
      e.target.parentNode.removeChild(e.target);
    });
  }
};

fetch("https://jsonplaceholder.typicode.com/albums")
  .then((res) => res.json())
  .then((data) => {
    useData(data);
  });

function useData(users) {
  const container = document.getElementById("data-container");

  users.forEach((user) => {
    const div = document.createElement("div");
    div.classList.add("card");
    div.innerHTML = `
      <h1>${user.id}</h1>
      <p>${user.title}</p>
    `;
    container.appendChild(div);
  });
}
