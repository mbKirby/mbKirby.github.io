(() => {
  "use strict";

  const yearElement = document.getElementById("currentYear");

  if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
  }

  // Close Bootstrap's mobile menu after choosing an in-page navigation link.
  const navCollapse = document.getElementById("primaryNav");

  if (navCollapse && window.bootstrap) {
    const navLinks = navCollapse.querySelectorAll("a.nav-link");

    navLinks.forEach((link) => {
      link.addEventListener("click", () => {
        if (window.innerWidth < 992 && navCollapse.classList.contains("show")) {
          const collapseInstance = bootstrap.Collapse.getOrCreateInstance(navCollapse);
          collapseInstance.hide();
        }
      });
    });
  }
})();
