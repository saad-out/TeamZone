$(document).ready(function () {
    const currentUserId = $("#current-user-id").val();
    const displayteams = $("#display-teams");

    $.ajax({
        url: apiUrl + "/api/v1/users/" + currentUserId + "/teams",
        type: "GET",
        contentType: "application/json",
        success: function (teams) {
            // remove the current content of displayteams
            displayteams.empty();

            // for each team, create a div with the team name, bio, city, country & image, and append it to the displayteams div
            if (teams.length > 0) {
                let teamsHTML = "";
                for (const team of teams) {
                    teamsHTML += `
                    <div class="col-lg-6">
                      <div class="card text-center">
                        <div class="card-header d-flex justify-content-between align-items-center">
                          <img src="/static/images/teams/${team.image}" alt="Team Logo"
                            class="img-fluid img-thumbnail rounded-circle img-sm" style="height: 50px; width: 50px" />
              
                          <span>${team.name}</span>
                          <div></div>
                          ${(currentUserId == team.leader_id) ? '<i class="bi bi-award">L</i>' : ''}
                        </div>
                        <div class="card-body">
                          <!--<h5 class="card-title">Team bio</h5>-->
                          <div class="row">
                            <div class="col-lg-6">
                              <i class="bi bi-geo-alt-fill"></i>
                              <span>${team.city}, ${team.country}</span>
                            </div>
                            <div class="col-lg-6">
                              <i class="bi bi-trophy-fill"></i>
                              <span>${team.sport}</span>
                            </div>
                          </div>
                          ${team.bio ? `<p class="card-text">${team.bio}</p>` : '<p class="card-text">No bio</p>'}
                          <a href="/myteams/${team.id}" class="btn btn-primary">Info</a>
                        </div>
                      </div>
                    </div>
                  `;
                }
                displayteams.html(`<div class="row">${teamsHTML}</div>`);
            } else {
                displayteams.html(`<h2 style="text-align: center;">You have no teams for the moment. Want to <a href="/myteams/create">create one</a> ?</h2>`);
            }

        },
        error: function (error) {
            console.log(error);
            displayteams.append("<p>There was an error retrieving your teams.</p>");
        }
    });
});