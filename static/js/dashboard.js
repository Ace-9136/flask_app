const links = document.querySelectorAll(".sidebar a");
const sections = document.querySelectorAll(".main section");

links.forEach((link) => {
  link.addEventListener("click", (event) => {
    event.preventDefault();
    const target = event.target.getAttribute("href");
    sections.forEach((section) => {
      section.style.display = "none";
    });
    document.querySelector(target).style.display = "block";
  });
});
