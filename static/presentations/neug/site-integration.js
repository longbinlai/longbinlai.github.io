// The site owns this copy of the deck, including its assets and interactions.
(() => {
  const language = new URLSearchParams(location.search).get('lang');
  if (language === 'en' || language === 'zh') window.neugSetLanguage?.(language);
  // Initialize the original deck's actual slide count, not its static placeholder.
  if (!location.hash) location.hash = 'slide-1';
})();
