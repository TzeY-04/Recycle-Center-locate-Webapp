const switchInput = document.getElementById("flexSwitchCheckDefault");
const modeIcon = document.getElementById("modeIcon");


if (localStorage.getItem("theme") === "dark") {
  document.body.classList.add("dark-mode");
  switchInput.checked = true;
  modeIcon.classList.replace("bi-moon-fill", "bi-sun-fill");
}

switchInput.addEventListener("change", () => {
  const isDark = switchInput.checked;
  document.body.classList.toggle("dark-mode", isDark);
  if (isDark) {
    modeIcon.classList.replace("bi-moon-fill", "bi-sun-fill");
  } else {
    modeIcon.classList.replace("bi-sun-fill", "bi-moon-fill");
  }
  localStorage.setItem("theme", isDark ? "dark" : "light");
});
