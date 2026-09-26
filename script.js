const toggle = document.querySelector('.nav-toggle');
const navigation = document.querySelector('#navigation');

if (toggle && navigation) {
  toggle.addEventListener('click', () => {
    const opening = toggle.getAttribute('aria-expanded') === 'false';
    toggle.setAttribute('aria-expanded', String(opening));
    toggle.querySelector('.sr-only').textContent = opening ? 'Fermer le menu' : 'Ouvrir le menu';
    navigation.classList.toggle('open', opening);
  });

  navigation.addEventListener('click', ({ target }) => {
    if (target.closest('a')) {
      toggle.setAttribute('aria-expanded', 'false');
      toggle.querySelector('.sr-only').textContent = 'Ouvrir le menu';
      navigation.classList.remove('open');
    }
  });
}

const toast = document.querySelector('.demo-toast');
let toastTimer;

document.querySelectorAll('[data-demo-action]').forEach((button) => {
  button.addEventListener('click', () => {
    window.clearTimeout(toastTimer);
    toast.hidden = false;
    toastTimer = window.setTimeout(() => { toast.hidden = true; }, 4000);
  });
});
