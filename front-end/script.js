document.getElementById('verify-button').addEventListener('click', function() {
    // Verify all required inputs are met
    if (validation() == false) {
        alert("Please fill in all required fields before submitting. Required fields are marked with a *.");
        return false;
    } else {
        // Move the logo
        const logo = document.querySelector('.logo');
        logo.style.transform = 'translate(0%)';
        logo.style.left = '100px'; // Adjust the final position as needed

        // Move and show the search bars
        const searchBars = document.querySelectorAll('.search-bar');
        searchBars.forEach((searchBar, index) => {
            setTimeout(() => {
                searchBar.style.opacity = '1';
                searchBar.style.transform = 'translateX(-34%)';
                searchBar.style.display = 'block';

                // Check if this is the last search bar
                if (index === searchBars.length - 1) {
                    // Move the button after the last search bar
                    const button = document.querySelector('.verify-button');
                    setTimeout(() => {
                        button.style.transform = 'translateX(-34%)';
                        const textbox = document.getElementById('result_text');
                        textbox.style.display = 'block';
                        setTimeout(() => {
                            textbox.style.opacity = '1';
                        }, 100);
                        }, 200);
                }
            }, 200 * (index + 1)); // Adjust the delay as needed for a staggered effect
        });
    }
});

function validation() {
  // Check if any input field is empty
  const link = document.getElementById("link_search").value;
  const website = document.getElementById("website_search").value;
  if (
    link === "" ||
    link === null ||
    website === "" ||
    website === null
  ) {
    return false; // Prevent form submission
  }

  return true;
}
