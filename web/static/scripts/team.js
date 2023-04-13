
$(document).ready(function () {

  const currentUserId = $("#current-user-id").val();
  const currentTeamId = $("#current-team-id").val();

  $("#team-card").append(`<div class="d-flex justify-content-center align-items-center">
                            <div class="spinner-grow" style="width: 3rem; height: 3rem;" role="status">
                              <span class="sr-only"></span>
                            </div>
                          </div>`);
  $("#team-players").append(`<div class="d-flex justify-content-center align-items-center">
                          <div class="spinner-grow" style="width: 3rem; height: 3rem;" role="status">
                            <span class="sr-only"></span>
                          </div>
                        </div>`);

  // get the team data from the API
  $.ajax({
    url: apiUrl + "/api/v1/teams/" + currentTeamId,
    type: "GET",
    dataType: "json",
    contentType: "application/json",
    success: function (team) {

      // populate the #team-info div with the team data
      $("#team-card").empty();
      $("#team-card").append(`<img
            src="/static/images/teams/${team.image}"
            alt="Team Logo"
            class="img-fluid rounded-circle w-50 h-50 mx-auto d-block"
            style="max-width: 100%; height: auto"
          />
          <h5 class="card-title">Team Details</h5>
          <div class="row">
            <div class="col-lg-3 col-md-4 label">Name</div>
            <div class="col-lg-9 col-md-8">${team.name}</div>
          </div>
          <div class="row">
            <div class="col-lg-3 col-md-4 label">Sport Type</div>
            <div class="col-lg-9 col-md-8">${team.sport}</div>
          </div>
          <div class="row">
            <div class="col-lg-3 col-md-4 label">Location</div>
            <div class="col-lg-9 col-md-8">
              ${team.city}, ${team.country}
            </div>
          </div>`);

      // populate the #team-players div with the team players
      $("#team-players").empty();
      $("#team-players").append(`<li
      class="list-group-item"
      style="
        display: flex;
        align-items: center;
        justify-content: space-between;
      "
    >
      ${team.leader}
      <i class="bi bi-award" style="margin-left: auto">Team Leader</i>
    </li>`);

      team.players.forEach(player => {
        if (player !== team.leader) {
          $("#team-players").append(`<li class="list-group-item">${player}</li>`);
        }
      });

    },
    error: function (error) {
      $("#team-card").append(`<p>Error while loading team !</p>`);
    }
  });

  const checkbox = document.querySelector("#reset-picture");
  const imgInput = document.querySelector("#image");
  if (checkbox !== null) {
    checkbox.addEventListener("change", () => {
      imgInput.disabled = checkbox.checked;
    });
  }

  // When the form is submitted, validate the data
  $("#edit-team-form").submit(function (event) {
    event.preventDefault();

    // if checkbox input is checked, assign "team_default.jpg" to const image, otherwise assign the value of the input filetype if an image is uploaded
    const image = checkbox.checked ? "team_default.jpg" : imgInput.value;

    let imageFileName = "team_default.jpg";
    // if the image is not the default image and not empty, send it in a POST to /myteams/currentTeamId/image
    if (image !== "team_default.jpg" && image !== "") {
      const formData = new FormData();
      formData.append("image", imgInput.files[0]);
      $.ajax({
        url: "/myteams/" + currentTeamId + "/image",
        type: "POST",
        dataType: "json",
        data: formData,
        contentType: false,
        processData: false,
        success: function (image) {
          imageFileName = image.filename;
          updateTeam(imageFileName);
        },
        error: function (error) {
          updateTeam("team_default.jpg");
        }
      });
    } else {
      updateTeam(imageFileName);
    }


    function updateTeam(image) {

      // get teamname, teamcity, teamcountry, teambio, teamsportId
      const teamName = $("#teamname").val();
      const teamCity = $("#teamcity").val();
      const teamCountry = $("#teamcountry").val();
      const teamBio = $("#teambio").val();
      const teamSportId = $("#teamsport").val();

      // make a put request to /api/v1/users/currentUserId/teams with the data type returned as JSON and the data as a JSON object using AJAX
      $.ajax({
        url: apiUrl + "/api/v1/users/" + currentUserId + "/teams/" + currentTeamId,
        type: "PUT",
        dataType: "json",
        data: JSON.stringify({
          name: teamName,
          city: teamCity,
          country: teamCountry,
          bio: teamBio,
          sport_id: teamSportId,
          image: image
        }),
        contentType: "application/json",
        success: function (team) {
          // redirect to /myteams/currentTeamId
          window.location.href = "/myteams/" + team.id;
        },
        error: function (error) {
          // redirect to /myteams/currentTeamId
          window.location.href = "/myteams/" + currentTeamId;
        }
      });
    }

  });
});
