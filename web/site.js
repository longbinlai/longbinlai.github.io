const search = document.querySelector('#paper-search');
const year = document.querySelector('#paper-year');
if (search && year) {
  const papers = [...document.querySelectorAll('[data-paper]')];
  const update = () => {
    let count = 0;
    for (const paper of papers) {
      const show = paper.textContent.toLowerCase().includes(search.value.trim().toLowerCase()) && (!year.value || paper.dataset.year === year.value);
      paper.hidden = !show;
      count += Number(show);
    }
    document.querySelector('#result-count').textContent = document.documentElement.lang === 'zh-CN' ? `共 ${count} 篇论文` : `${count} publications`;
    document.querySelector('#no-results').hidden = count !== 0;
  };
  search.addEventListener('input', update);
  year.addEventListener('change', update);
  update();
}

const qrDialog = document.querySelector('#qr-dialog');
if (qrDialog) {
  let opener;
  document.querySelectorAll('.qr-open').forEach(button => button.addEventListener('click', () => {
    opener = button;
    qrDialog.showModal();
  }));
  qrDialog.querySelector('.qr-close').addEventListener('click', () => qrDialog.close());
  qrDialog.addEventListener('close', () => opener?.focus());
}
