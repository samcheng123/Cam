document.documentElement.classList.add('js');
const menuToggle = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
if (menuToggle && navigation) {
  menuToggle.addEventListener('click', () => {
    const open = menuToggle.getAttribute('aria-expanded') !== 'true';
    menuToggle.setAttribute('aria-expanded', String(open));
    navigation.classList.toggle('is-open', open);
    menuToggle.textContent = open ? 'close ×' : 'menu ☰';
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menuToggle.getAttribute('aria-expanded') === 'true') {
      menuToggle.click();
      menuToggle.focus();
    }
  });
}
const search = document.querySelector('#publication-search');
if (search) {
  let category = 'all';
  const papers = [...document.querySelectorAll('[data-publication]')];
  const buttons = [...document.querySelectorAll('[data-filter]')];
  const update = () => {
    const query = search.value.trim().toLocaleLowerCase();
    let count = 0;
    for (const paper of papers) {
      const visible = (category === 'all' || paper.dataset.category === category) && paper.textContent.toLocaleLowerCase().includes(query);
      paper.hidden = !visible;
      count += Number(visible);
    }
    document.querySelectorAll('.publication-group').forEach(group => {
      group.hidden = ![...group.querySelectorAll('[data-publication]')].some(paper => !paper.hidden);
    });
    document.querySelector('#results-status').textContent = `${count} of ${papers.length} publications`;
    document.querySelector('#empty-state').hidden = count !== 0;
  };
  search.addEventListener('input', update);
  buttons.forEach(button => button.addEventListener('click', () => {
    category = button.dataset.filter;
    buttons.forEach(other => other.setAttribute('aria-pressed', String(other === button)));
    update();
  }));
}
