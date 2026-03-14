class DarkMode {
  constructor() {
    this.theme = localStorage.getItem('theme') || 'light';
    this.toggleButton = document.getElementById('dark-mode-toggle');
    this.applyTheme();
    this.toggleButton.addEventListener('click', () => this.toggleTheme());
  }

  applyTheme() {
    if (this.theme === 'dark') {
      document.body.classList.add('dark-mode');
    } else {
      document.body.classList.remove('dark-mode');
    }
  }

  toggleTheme() {
    if (this.theme === 'dark') {
      this.theme = 'light';
    } else {
      this.theme = 'dark';
    }
    localStorage.setItem('theme', this.theme);
    this.applyTheme();
  }
}

const darkMode = new DarkMode();