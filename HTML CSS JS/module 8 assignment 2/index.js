const fetchAllDrinks = (name = "margarita") => {
  fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${name}`)
    .then((res) => res.json())
    .then((data) => setCards(data.drinks));
};

fetchAllDrinks();

const setCards = (data) => {
  const cardContainer = document.getElementById("card-container");
  if (!data) {
    cardContainer.innerHTML = `
        <h1 class="text-center w-100">No Drinks Found</h1>
    `;
  } else {
    data.forEach((drink) => {
      const div = document.createElement("div");
      div.innerHTML = `
            <div class="card" style="width: 18rem;">
            <img src="${drink.strDrinkThumb}" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Name: ${drink.strGlass}</h5>
                <h6 class="card-title">Category: ${drink.strCategory}</h6>
                <p class="card-text">Instructions: ${drink.strInstructions.slice(
                  0,
                  30
                )}...</p>
                <div class="d-flex justify-content-between">
                <button type="button" class="btn btn-primary" id="add-to-cart"
                onclick="addToCart('${drink.strDrinkThumb}','${
        drink.strGlass
      }')">Add to Cart</button>
                <button type="button" class="btn btn-info" id="details"
                onclick="showDetails('${drink.idDrink}')">Show Details</button>
                </div>
            </div>
            </div>
        `;
      cardContainer.appendChild(div);
    });
  }
};

document.getElementById("search-btn").addEventListener("click", () => {
  const name = document.getElementById("search-field").value;

  document.getElementById("card-container").innerHTML = "";
  fetchAllDrinks(name);
});

const showDetails = (id) => {
  fetch(`https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=${id}`)
    .then((res) => res.json())
    .then((data) => {
      const drink = data.drinks[0];
      const modalBody = document.getElementById("modal-body-content");
      modalBody.innerHTML = `
        <div class="text-center">
          <img src="${drink.strDrinkThumb}" class="img-fluid mb-3" alt="${drink.strDrink}" style="max-height: 300px;">
        </div>
        <h3>${drink.strDrink}</h3>
        <p><strong>Category:</strong> ${drink.strCategory}</p>
        <p><strong>Glass:</strong> ${drink.strGlass}</p>
        <p><strong>Instructions:</strong> ${drink.strInstructions}</p>
      `;

      const myModal = new bootstrap.Modal(
        document.getElementById("drinkModal")
      );
      myModal.show();
    });
};

let count = 0;

const addToCart = (img, name) => {
  if (count > 6) {
    alert("can not add more than 7 drinks.");
    return;
  }

  document.getElementById("total").innerText = count + 1;
  const table = document.getElementById("t-body");
  const tr = document.createElement("tr");
  count++;
  tr.innerHTML = `
                <th scope="row">${count}</th>
                <td><img src="${img}" alt="" style="width: 40px; border-radius: 50%;"></td>
                <td>${name}</td>
      `;
  table.appendChild(tr);
};
