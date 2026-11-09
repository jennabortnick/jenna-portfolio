(() => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  const closeMenu = () => { nav?.classList.remove('open'); toggle?.setAttribute('aria-expanded', 'false'); };
  toggle?.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open)); nav.classList.toggle('open', open);
  });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeMenu(); });
  nav?.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
  const filters = document.querySelectorAll('[data-filter]');
  filters.forEach(button => button.addEventListener('click', () => {
    const filter = button.dataset.filter;
    filters.forEach(b => b.setAttribute('aria-pressed', String(b === button)));
    document.querySelectorAll('[data-category]').forEach(section => section.hidden = filter !== 'all' && section.dataset.category !== filter);
    const status = document.querySelector('#filter-status');
    if (status) status.textContent = filter === 'all' ? 'Showing all 8 projects.' : filter === 'themed' ? 'Showing 6 themed entertainment projects.' : 'Showing 2 Blender projects.';
  }));
  const dialog = document.querySelector('.lightbox');
  const image = dialog?.querySelector('img');
  const caption = dialog?.querySelector('.lightbox-caption');
  document.querySelectorAll('[data-lightbox]').forEach(button => button.addEventListener('click', () => {
    image.src = button.dataset.lightbox;
    image.alt = button.dataset.caption || '';
    caption.textContent = button.dataset.caption || '';
    dialog.showModal(); document.body.classList.add('locked');
  }));
  dialog?.querySelector('.lightbox-close').addEventListener('click', () => dialog.close());
  dialog?.addEventListener('click', event => { if (event.target === dialog) { const r = dialog.getBoundingClientRect(); if (event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) dialog.close(); } });
  dialog?.addEventListener('close', () => { document.body.classList.remove('locked'); image.removeAttribute('src'); });
})();
