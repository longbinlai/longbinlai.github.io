(() => {
  let saved;
  try { saved = localStorage.getItem('theme'); } catch {}
  const media = matchMedia('(prefers-color-scheme: dark)');
  const apply = (theme) => {
    document.documentElement.dataset.theme = theme;
    document.querySelector('meta[name="theme-color"]')?.setAttribute('content', theme === 'dark' ? '#101010' : '#fafafa');
    const button = document.querySelector('#theme-toggle');
    if (button) {
      button.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
      button.setAttribute('aria-pressed', String(theme === 'dark'));
    }
  };
  apply(saved === 'light' || saved === 'dark' ? saved : media.matches ? 'dark' : 'light');
  media.addEventListener('change', () => { if (!saved) apply(media.matches ? 'dark' : 'light'); });
  document.addEventListener('DOMContentLoaded', () => {
    apply(document.documentElement.dataset.theme);
    document.querySelector('#theme-toggle')?.addEventListener('click', () => {
      saved = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem('theme', saved); } catch {}
      apply(saved);
    });
  });
})();
