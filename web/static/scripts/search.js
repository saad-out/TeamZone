$(document).ready(function () {
    const data = {
        countries: {},
        cities: {},
        sports: {},
    };
    const checkboxes = document.querySelectorAll(".filter-checkbox");
    const countriesShow = document.querySelector(".countriesShow");
    const citiesShow = document.querySelector(".citiesShow");
    const sportsShow = document.querySelector(".sportsShow");
    const searchBtn = document.querySelector("#search-btn");
    const searchResult = document.querySelector("#search-result");

    checkboxes.forEach((checkbox) => {
        checkbox.addEventListener("click", (event) => {
            const dataName = event.target.getAttribute("data-name");
            const dataId = event.target.getAttribute("data-id");

            if (event.target.classList.contains("country")) {
                if (event.target.checked) {
                    data.countries[dataId] = dataName;
                } else {
                    delete data.countries[dataId];
                }
                countriesShow.placeholder = Object.values(data.countries).join(", ");
                if (countriesShow.placeholder == "") {
                    countriesShow.placeholder = "Select countries";
                }
            }
            if (event.target.classList.contains("city")) {
                if (event.target.checked) {
                    data.cities[dataId] = dataName;
                } else {
                    delete data.cities[dataId];
                }
                citiesShow.placeholder = Object.values(data.cities).join(", ");
                if (citiesShow.placeholder == "") {
                    citiesShow.placeholder = "Select cities";
                }
            }
            if (event.target.classList.contains("sport")) {
                if (event.target.checked) {
                    data.sports[dataId] = dataName;
                } else {
                    delete data.sports[dataId];
                }
                sportsShow.placeholder = Object.values(data.sports).join(", ");
                if (sportsShow.placeholder == "") {
                    sportsShow.placeholder = "Select sports";
                }
            }
        });
    });

    async function postData(url = "", data = {}) {
        postdata = {};
        postdata.countries = Object.keys(data.countries);
        postdata.cities = Object.keys(data.cities);
        postdata.sports = Object.keys(data.sports);

        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(postdata),
        });

        return response.json();
    }

    function populateSearch(teams) {
        if (teams.length == 0) {
            searchResult.innerHTML = "<p>No result found</p>";
            return;
        }
        searchResult.innerHTML = `<p>Teams found (${teams.length})</p>`;
        for (const team of teams) {
            searchResult.innerHTML += `<div class="col-lg-12">
            <div class="card text-center">
              <div class="card-header">${team.name}</div>
              <div class="card-body">
                <div class="row">
                  <div class="col-lg-4">
                    <i class="bi bi-geo-alt-fill"></i>
                    <span>${team.city}, ${team.country}</span>
                  </div>
                  <div class="col-lg-4"></div>
                  <div class="col-lg-4">
                    <i class="bi bi-trophy-fill"></i>
                    <span>${team.sport}</span>
                  </div>
                </div>
                <p class="card-text">${team.bio}</p>
                <a href="/search/${team.id}" class="btn btn-primary">Connect</a>
              </div>
            </div>
          </div>`;
        }
    }

    searchBtn.addEventListener("click", () => {
        searchResult.innerHTML = `<div class="spinner-border" style="width: 50px; height: 50px;" role="status">
                    <span class="visually-hidden">Loading...</span>
                  </div>`;
        url = "http://127.0.0.1:5001/api/v1/filter_teams";
        returnedData = postData(url, data);
        returnedData.then((teams) => {
            console.log(teams);
            populateSearch(teams);
        });
    });

    // Get the country list container and items
    var countryListContainer = $("#inner-box1");
    var countryItems = $(".country-item");

    // Listen for changes to the search input field
    $("#country-search").on("input", function () {
        // Get the search term and convert to lowercase
        var searchTerm = $(this).val().toLowerCase();

        // Loop through each country item
        countryItems.each(function () {
            var countryName = $(this).find(".tick").text().toLowerCase();
            // Check if the country name matches the search term
            if (countryName.indexOf(searchTerm) === -1) {
                // Hide the item if it doesn't match
                $(this).hide();
            } else {
                // Show the item if it does match
                $(this).show();
            }
        });
    });

});