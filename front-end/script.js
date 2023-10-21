document.addEventListener("DOMContentLoaded", function () {
    const logo = document.getElementById("logo");
    const searchButton = document.getElementById("search-button");
  
    searchButton.addEventListener("click", function () {
      logo.style.transform = "translateX(-100px)";
    });
  });
  