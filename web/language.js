(() => {
  const zh = document.documentElement.lang === 'zh-CN';
  const link = document.querySelector('.language-toggle');
  link?.addEventListener('click', () => {
    try { localStorage.setItem('language', zh ? 'en' : 'zh'); } catch {}
  });
  // Restore a visitor's explicit language preference on the main entry page.
  if (location.pathname === '/') {
    try { if (localStorage.getItem('language') === 'zh') location.replace('/zh/' + location.search + location.hash); } catch {}
  }
  const themeButton = document.querySelector('#theme-toggle');
  if (zh && themeButton) {
    const label = () => themeButton.setAttribute('aria-label', document.documentElement.dataset.theme === 'dark' ? '切换到白天模式' : '切换到黑夜模式');
    label();
    themeButton.addEventListener('click', label);
    new MutationObserver(label).observe(document.documentElement, {attributes:true, attributeFilter:['data-theme']});
  }
})();
