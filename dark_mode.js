const darkModeToggle = document.getElementById('dark-mode-toggle');
const body = document.body;
let isDarkMode = false;

// Load saved theme preference
if (localStorage.getItem('darkMode') === 'true') {
  isDarkMode = true;
  body.classList.add('dark-mode');
}

// Toggle dark mode
darkModeToggle.addEventListener('click', () => {
  isDarkMode = !isDarkMode;
  body.classList.toggle('dark-mode', isDarkMode);
  localStorage.setItem('darkMode', isDarkMode);
});