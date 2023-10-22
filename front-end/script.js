document.addEventListener("DOMContentLoaded", function () {
  const logo = document.getElementById("logo");
  const searchButton = document.querySelector("button[type='submit']");
  const cover = document.getElementById("cover");
  const darkModeButton = document.getElementById("dark-mode-button");
  const body = document.body;

  const isDarkModeEnabled = localStorage.getItem("darkModeEnabled") === "true";
  
  function toggleDarkMode() {
    body.classList.toggle("dark-mode");
    const darkModeEnabled = body.classList.contains("dark-mode");
    localStorage.setItem("darkModeEnabled", darkModeEnabled);
  }
  
  searchButton.addEventListener("click", function (e) {
    e.preventDefault(); // Prevent form submission
    logo.classList.add("move-left");
    cover.classList.add("move-up"); 
  });
  darkModeButton.addEventListener("click", toggleDarkMode);
});
