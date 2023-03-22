/*const toggleBtn = document.getElementById("toggle-btn");
const team = document.getElementById("team-info");
const myForm = document.getElementById("edit-team");

toggleBtn.addEventListener("click", function () {
  if (myForm.style.display == "none" || myForm.style.display == "") {
    myForm.style.display = "block";
    team.style.display = "none";
    toggleBtn.innerHTML = '<i class="bi bi-x-square me-1"></i> Stop Editing';
  } else {
    myForm.style.display = "none";
    team.style.display = "block";
    toggleBtn.innerHTML = '<i class="bi bi-pencil-square me-1"></i> Edit Team';
  }
});*/

const checkbox = document.querySelector("#reset-picture");
const imgInput = document.querySelector("#image");
checkbox.addEventListener("change", () => {
  imgInput.disabled = checkbox.checked;
});
