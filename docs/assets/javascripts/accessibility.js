/* Make Material's label-based toggles keyboard-operable without changing its state model. */
function enhanceLedgerlyControls() {
  document.querySelectorAll('label.md-header__button[for], label.md-nav__link[for]').forEach(label => {
    const id = label.getAttribute('for');
    const input = document.getElementById(id);
    if (!input || label.dataset.ledgerlyAccessible) return;
    label.dataset.ledgerlyAccessible = 'true';
    label.setAttribute('role', 'button');
    label.setAttribute('tabindex', '0');
    const name = label.title || (id === '__drawer' ? 'Open navigation menu' : id === '__search' ? 'Open documentation search' : label.textContent.trim());
    label.setAttribute('aria-label', name);
    if (input.type === 'checkbox') {
      const update = () => label.setAttribute('aria-expanded', String(input.checked));
      input.addEventListener('change', update); update();
    }
    label.addEventListener('keydown', event => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault(); event.stopPropagation();
        input.checked = input.type === 'radio' || !input.checked;
        input.dispatchEvent(new Event('change', {bubbles: true}));
      }
    });
  });
  document.addEventListener('keydown', event => {
    const drawer = document.getElementById('__drawer');
    if (event.key === 'Escape' && drawer?.checked) {
      drawer.checked = false;
      drawer.dispatchEvent(new Event('change', {bubbles: true}));
      document.querySelector('header label[for="__drawer"]')?.focus();
    }
  });
}
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', enhanceLedgerlyControls);
else enhanceLedgerlyControls();
