/* Shared controls without third-party runtime dependencies. */
(() => {
  'use strict';

  const toggle = document.querySelector('[data-menu-toggle]');
  if (toggle) {
    const menu = document.getElementById(toggle.getAttribute('aria-controls'));
    toggle.addEventListener('click', () => {
      const expanded = toggle.getAttribute('aria-expanded') !== 'true';
      toggle.setAttribute('aria-expanded', String(expanded));
      menu.classList.toggle('show', expanded);
    });
    menu.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        menu.classList.remove('show');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  document.querySelectorAll('[data-site-tabs]').forEach((group) => {
    const tabs = Array.from(group.querySelectorAll('[role="tab"]'));
    const select = (selected) => tabs.forEach((tab) => {
      const active = tab === selected;
      tab.setAttribute('aria-selected', String(active));
      tab.tabIndex = active ? 0 : -1;
      tab.classList.toggle('active', active);
      const panel = document.getElementById(tab.getAttribute('aria-controls'));
      panel.hidden = !active;
      panel.classList.toggle('active', active);
    });
    tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => select(tab));
      tab.addEventListener('keydown', (event) => {
        let next;
        if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
        if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
        if (event.key === 'Home') next = 0;
        if (event.key === 'End') next = tabs.length - 1;
        if (next !== undefined) {
          event.preventDefault();
          select(tabs[next]);
          tabs[next].focus();
        }
      });
    });
  });

  const images = Array.from(document.querySelectorAll('a.image-popup'));
  if (!images.length || typeof HTMLDialogElement === 'undefined') return;

  const dialog = document.createElement('dialog');
  dialog.className = 'r-lightbox';
  dialog.setAttribute('aria-label', 'Просмотр фотографий');
  dialog.innerHTML = '<button type="button" class="r-lightbox-close" aria-label="Закрыть">×</button>' +
    '<button type="button" class="r-lightbox-prev" aria-label="Предыдущее фото">‹</button>' +
    '<figure><img alt=""><figcaption aria-live="polite"></figcaption></figure>' +
    '<button type="button" class="r-lightbox-next" aria-label="Следующее фото">›</button>';
  document.body.append(dialog);
  const picture = dialog.querySelector('img');
  const caption = dialog.querySelector('figcaption');
  let current = 0;
  let opener;
  const show = (index) => {
    current = (index + images.length) % images.length;
    const link = images[current];
    picture.src = link.href;
    picture.alt = link.getAttribute('aria-label') || link.getAttribute('alt') || 'Фотография выполненной работы';
    caption.textContent = `${current + 1} / ${images.length} — ${picture.alt}`;
  };
  images.forEach((link, index) => link.addEventListener('click', (event) => {
    if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    opener = link;
    show(index);
    dialog.showModal();
    document.body.classList.add('r-lightbox-open');
  }));
  dialog.querySelector('.r-lightbox-close').addEventListener('click', () => dialog.close());
  dialog.querySelector('.r-lightbox-prev').addEventListener('click', () => show(current - 1));
  dialog.querySelector('.r-lightbox-next').addEventListener('click', () => show(current + 1));
  dialog.querySelectorAll('.r-lightbox-prev, .r-lightbox-next').forEach((button) => {
    button.hidden = images.length < 2;
  });
  dialog.addEventListener('click', (event) => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
      event.preventDefault();
      show(current + (event.key === 'ArrowRight' ? 1 : -1));
    }
  });
  dialog.addEventListener('close', () => {
    document.body.classList.remove('r-lightbox-open');
    picture.removeAttribute('src');
    if (opener) opener.focus();
  });
})();
