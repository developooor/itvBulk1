const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('#nav-links');

if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    const isOpen = navToggle.getAttribute('aria-expanded') === 'true';
    navToggle.setAttribute('aria-expanded', String(!isOpen));
    navToggle.querySelector('.sr-only').textContent = isOpen ? 'Open navigation' : 'Close navigation';
    navLinks.classList.toggle('open', !isOpen);
  });

  navLinks.addEventListener('click', (event) => {
    if (event.target.closest('a')) {
      navToggle.setAttribute('aria-expanded', 'false');
      navToggle.querySelector('.sr-only').textContent = 'Open navigation';
      navLinks.classList.remove('open');
    }
  });
}

document.querySelector('#year').textContent = new Date().getFullYear();
