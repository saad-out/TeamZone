$(document).ready(function () {
    // Load the countries in the select bar
    $.get("https://restcountries.com/v3.1/all", function (data) {
        for (var i = 0; i < data.length; i++) {
            var country = data[i];
            $("#teamcountry").append($("<option>").attr("value", country.name.common).text(country.name.common));
        }
    });

    // When a country is selected, load the cities of that country
    $("#teamcountry").change(function () {
        var countryName = $(this).val();
        if (countryName) {
            $("#teamcity").prop("disabled", false);
            $("#teamcity").empty().append($("<option>").attr("value", "").text("Choose..."));
            $.get("https://countriesnow.space/api/v0.1/countries/cities/q", { country: countryName }, function (data) {
                if (data.error) {
                    alert("Error: " + data.msg);
                    return;
                }
                var cities = data.data;
                for (var i = 0; i < cities.length; i++) {
                    var city = cities[i];
                    $("#teamcity").append($("<option>").attr("value", city).text(city));
                }
            });
        } else {
            $("#teamcity").prop("disabled", true);
        }
    });

    // When the form is submitted, validate the data
    $("#teamform").submit(function (event) {
        event.preventDefault();

        // get current user id from input with id current-user-id
        var currentUserId = $("#current-user-id").val();
        // get teamname, teamcity, teamcountry, teambio, teamsportId
        var teamName = $("#teamname").val();
        var teamCity = $("#teamcity").val();
        var teamCountry = $("#teamcountry").val();
        var teamBio = $("#teambio").val();
        var teamSportId = $("#teamsport").val();

        // make a post request to /api/v1/users/currentUserId/teams with the data type returned as JSON and the data as a JSON object using AJAX
        $.ajax({
            url: "http://localhost:5001/api/v1/users/" + currentUserId + "/teams",
            type: "POST",
            dataType: "json",
            data: JSON.stringify({
                name: teamName,
                city: teamCity,
                country: teamCountry,
                bio: teamBio,
                sport_id: teamSportId
            }),
            contentType: "application/json",
            success: function (team) {
                window.location.href = "/myteams/" + team.id;              
            },
            error: function (data) {
                async function postData() {
                    const response = await $.post("/flashed", { message: "Unsuccessful team creation !", category: "error" });
                    window.location.href = "/myteams";
                };
                postData();
            }
        });
    });

});