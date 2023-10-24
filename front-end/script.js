document.addEventListener("DOMContentLoaded", function () {
  const logo = document.getElementById("logo");
  const searchButton = document.querySelector("button[type='submit']");
  const cover = document.getElementById("cover");
  const darkModeButton = document.getElementById("dark-mode-button");
  const body = document.body;
  const searchInput = document.querySelector("input[type='text']");

  const isDarkModeEnabled = localStorage.getItem("darkModeEnabled") === "true";

  function toggleDarkMode() {
    body.classList.toggle("dark-mode");
    const darkModeEnabled = body.classList.contains("dark-mode");
    localStorage.setItem("darkModeEnabled", darkModeEnabled);
  }

  searchButton.addEventListener("click", function (e) {
    e.preventDefault(); // Prevent form submission

    const searchTerm = searchInput.value.trim();

    if (searchTerm === "") {
      alert("Input URL to begin the operation");
    } else if (!isValidURL(searchTerm)) {
      showError("Cannot Identify URL Please Try Again!");
    } else {
      logo.classList.add("move-left");
      cover.classList.add("move-up");
    }
  });

  darkModeButton.addEventListener("click", toggleDarkMode);

  // Function to check if a string is a valid URL
  function isValidURL(str) {
    const pattern = new RegExp(
      "^(https?:\\/\\/)?" +
      "((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|" +
      "((\\d{1,3}\\.){3}\\d{1,3}))" +
      "(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*" +
      "(\\?[;&a-z\\d%_.~+=-]*)?" +
      "(\\#[-a-z\\d_]*)?$",
      "i"
    );
    return !!pattern.test(str);
  }

  // Function to display an error message with a blink animation
  function showError(message) {
    const errorElement = document.createElement("div");
    errorElement.textContent = message;
    errorElement.classList.add("error-message");
    searchInput.parentElement.appendChild(errorElement); // Append the error message outside the search bar

    // Remove the error message after 2 seconds
    setTimeout(function () {
      errorElement.remove();
    }, 2000);

    // Add a class for blinking animation
    setTimeout(function () {
      errorElement.classList.add("blink");
    }, 100);

    // Remove the blinking class after 1.5 seconds
    setTimeout(function () {
      errorElement.classList.remove("blink");
    }, 1500);
  }
});
