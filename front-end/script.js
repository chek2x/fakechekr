document.addEventListener("DOMContentLoaded", function () {
  const logo = document.getElementById("logo");
  const searchButton = document.querySelector("button[type='submit']");
  const cover = document.getElementById("cover");

  searchButton.addEventListener("click", function (e) {
    e.preventDefault(); // Prevent form submission
    logo.classList.add("move-left");
    cover.classList.add("move-up"); 
  });
});
