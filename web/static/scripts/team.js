
$(document).ready(function () {

  const checkbox = document.querySelector("#reset-picture");
  const imgInput = document.querySelector("#image");
  checkbox.addEventListener("change", () => {
    imgInput.disabled = checkbox.checked;
  });

  const currentUserId = $("#current-user-id").val();
  const currentTeamId = $("#current-team-id").val();

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
          console.log("Image uploaded successfully");
          imageFileName = image.filename;
          console.log(imageFileName);
          updateTeam(imageFileName);
        },
        error: function (error) {
          console.log("Error uploading image");
          console.log(error);
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
          console.log(error);
          // redirect to /myteams/currentTeamId
          window.location.href = "/myteams/" + currentTeamId;
        }
      });
    }

  });
});
