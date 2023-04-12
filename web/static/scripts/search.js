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

  const searchResult = $("#search-result");
  const currentUserId = $("#current-user-id").val();

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

  let teams = [];
  let startIndex = 0;
  const teamsPerPage = 10;

  // Function to send JSON post request and retrieve teams
  function getTeams(postData) {
    $.ajax({
      url: apiUrl + "/api/v1/filter_teams",
      type: "POST",
      dataType: "json",
      data: JSON.stringify(postData),
      contentType: "application/json",
      success: function (response) {
        teams = response;
        startIndex = 0;
        searchResult.empty(); // Clear previous content
        searchResult.append(`<p>Teams found (${teams.length})</p>`);
        displayTeams();
      },
      error: function (data) {
        console.log(data);
        searchResult.empty();
        searchResult.append(`<p>Error while fetching teams !</p>`);
      }
    });
  }

  // Function to display teams
  function displayTeams() {
    for (let i = startIndex; i < startIndex + teamsPerPage && i < teams.length; i++) {
      let team = teams[i];
      console.log(team.name + String(i));
      searchResult.append(`<div class="col-lg-12">
      <div class="card text-center">
        <div class="card-header d-flex justify-content-between align-items-center">
          <img
            src="/static/images/teams/${team.image}"
            alt="Team Logo"
            class="img-fluid img-thumbnail rounded-circle img-sm"
            style="height: 50px; width: 50px"
          /><span>${team.name}</span>
          <div></div>
          ${(currentUserId == team.leader_id) ? '<i class="bi bi-award">L</i>' : ''}
        </div>
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
          ${team.bio ? `<p class="card-text">${team.bio}</p>` : `<p class="card-text">$No bio</p>`}
          <a href="/search/${team.id}" class="btn btn-primary">Connect</a>
        </div>
      </div>
    </div>`);
    }
  }

  // Function to handle scroll event
  function handleScroll() {
    const distanceToBottom = document.documentElement.offsetHeight - (window.innerHeight + window.pageYOffset);
    if (distanceToBottom < 500) {
      startIndex += teamsPerPage; // Increment startIndex
      displayTeams(); // Display next batch of teams
    }
  }

  searchBtn.addEventListener("click", (event) => {
    searchResult.empty();
    searchResult.append(`<div class="spinner-border" style="width: 50px; height: 50px;" role="status">
    <span class="visually-hidden">Loading...</span>
  </div>`);

    const filters = {};
    filters.countries = Object.keys(data.countries);
    filters.cities = Object.keys(data.cities);
    filters.sports = Object.keys(data.sports);

    getTeams(filters);

  });

  // Attach scroll event handler to window
  $(window).on('scroll', handleScroll);


  // Get the country list container and items
  var countryListContainer = $("#inner-box1");
  var countryItems = $(".country-item");
  var cityItems = $(".city-item");
  var sportItems = $(".sport-item");

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
  $("#city-search").on("input", function () {
    // Get the search term and convert to lowercase
    var searchTerm = $(this).val().toLowerCase();

    // Loop through each country item
    cityItems.each(function () {
      var cityName = $(this).find(".tick").text().toLowerCase();
      // Check if the city name matches the search term
      if (cityName.indexOf(searchTerm) === -1) {
        // Hide the item if it doesn't match
        $(this).hide();
      } else {
        // Show the item if it does match
        $(this).show();
      }
    });
  });
  $("#sport-search").on("input", function () {
    // Get the search term and convert to lowercase
    var searchTerm = $(this).val().toLowerCase();

    // Loop through each country item
    sportItems.each(function () {
      var sportName = $(this).find(".tick").text().toLowerCase();
      // Check if the sport name matches the search term
      if (sportName.indexOf(searchTerm) === -1) {
        // Hide the item if it doesn't match
        $(this).hide();
      } else {
        // Show the item if it does match
        $(this).show();
      }
    });
  });
});
