const toggleSidebar = document.getElementById("toggle-sidebar-btn");
const sidebar = document.querySelector(".sidebar");

toggleSidebar.addEventListener("click", () => {
  sidebar.classList.toggle("show");
});
