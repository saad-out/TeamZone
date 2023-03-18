const checkbox = document.querySelector("#reset-picture");
const imgInput = document.querySelector("#image");
checkbox.addEventListener("change", () => {
  imgInput.disabled = checkbox.checked;
});
