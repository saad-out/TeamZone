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
});