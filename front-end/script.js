document.getElementById("verify-button").addEventListener("click", function () {
  // Move the logo
  const logo = document.querySelector(".logo");
  logo.style.transform = "translate(0%)";
  logo.style.left = "100px"; // Adjust the final position as needed

  // Move and show the search bars
  const searchBars = document.querySelectorAll(".search-bar");
  searchBars.forEach((searchBar, index) => {
    setTimeout(() => {
      searchBar.style.opacity = "1";
      searchBar.style.transform = "translateX(-34%)";
      searchBar.style.display = "block";

      // Check if this is the last search bar
      if (index === searchBars.length - 1) {
        // Move the button after the last search bar
        const button = document.querySelector(".verify-button");
        setTimeout(() => {
          button.style.transform = "translateX(-34%)";
          const textbox = document.getElementById("result_text");
          textbox.style.display = "block";
          setTimeout(() => {
            textbox.style.opacity = "1";
          }, 100);
        }, 200);
      }
    }, 200 * (index + 1)); // Adjust the delay as needed for a staggered effect
  });
});

function submit_handler() {
  // Check if any input field is empty
  const link = document.getElementById("link_search").value;
  const website = document.getElementById("website_search").value;
  const headline = document.getElementById("headline_search").value;
  const authors = document.getElementById("authors_search").value;
  const body = document.getElementById("body_search").value;
  const date = document.getElementById("date_search").value;

  if (
    link === "" ||
    website === "" ||
    headline === "" ||
    authors === "" ||
    body === "" ||
    date === ""
  ) {
    alert("Please fill in all the fields before submitting.");
    return false; // Prevent form submission
  }
}

document.getElementById('verify-button').addEventListener('click', submit_handler);
