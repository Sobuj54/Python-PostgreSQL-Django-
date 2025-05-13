const fetchAllmeals = (name = "") => {
  fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${name}`)
    .then((res) => res.json())
    .then((data) => setCards(data.meals));
};

fetchAllmeals();

const setCards = (data) => {
  const cardContainer = document.getElementById("card-container");
  if (!data) {
    cardContainer.innerHTML = `
        <h1 class="text-center w-100">No Meals Found</h1>
    `;
  } else {
    data.forEach((meal) => {
      const div = document.createElement("div");
      div.innerHTML = `
            <div class="card" style="width: 18rem;">
            <img src="${meal.strMealThumb}" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Name: ${meal.strMeal}</h5>
                <h6 class="card-title">Category: ${meal.strCategory}</h6>
                <p class="card-text">Instructions: ${meal.strInstructions.slice(
                  0,
                  30
                )}...</p>
                <div class="d-flex justify-content-between">
                <button type="button" class="btn btn-info" id="details"
                onclick="showDetails('${meal.idMeal}')">Show Details</button>
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
  fetchAllmeals(name);
});

const showDetails = (id) => {
  fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`)
    .then((res) => res.json())
    .then((data) => addDetailCard(data.meals[0]));
};

const addDetailCard = (data) => {
  const modal = document.getElementById("top-modal");
  modal.innerHTML = "";
  const div = document.createElement("div");
  div.innerHTML = `
        <div class="card" style="width: 18rem;">
  <img src="${data.strMealThumb}" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">${data.strMeal}</h5>
    <p class="card-text">${data.strInstructions.slice(0, 200)}</p>
  </div>
</div>
    `;
  modal.appendChild(div);
};
