document.addEventListener("DOMContentLoaded", function () {
  const infoButtons = document.querySelectorAll(".info");

  const infoContainer = document.querySelector(".info-container");
  const infoContent = document.querySelector(".info-content");
  const infoText = document.querySelector(".info-text");

  infoButtons.forEach((button) => {
      button.addEventListener("click", (event) => {
          const info = event.target.getAttribute("data-info");
          infoText.innerHTML = info;
          infoContainer.classList.add("show");
      });
  });

  infoContent.addEventListener("click", () => {
      infoContainer.classList.remove("show");
  });
});
