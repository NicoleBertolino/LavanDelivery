// Abas "Assinatura individual" / "Pacote república" da página de planos.
(function () {
  const abas = document.querySelectorAll('.plan-tabs button');
  const indicador = document.getElementById('tab-indicator');
  if (!abas.length) return;

  function moverIndicador() {
    const ativa = document.querySelector('.plan-tabs button.active');
    if (ativa && indicador) {
      indicador.style.left = ativa.offsetLeft + 'px';
      indicador.style.width = ativa.offsetWidth + 'px';
    }
  }

  function selecionar(nome) {
    abas.forEach(function (b) {
      const ativa = b.dataset.plan === nome;
      b.classList.toggle('active', ativa);
      b.setAttribute('aria-selected', ativa ? 'true' : 'false');
    });
    document.querySelectorAll('.plan-sub').forEach(function (s) {
      s.classList.toggle('active', s.id === 'plan-' + nome);
    });
    moverIndicador();

    // Deixa o endereço compartilhável (?aba=republica) sem recarregar a página.
    const url = new URL(window.location.href);
    if (nome === 'individual') { url.searchParams.delete('aba'); } else { url.searchParams.set('aba', nome); }
    history.replaceState(null, '', url);
  }

  abas.forEach(function (b) {
    b.addEventListener('click', function () { selecionar(b.dataset.plan); });
  });
  window.addEventListener('resize', moverIndicador);
  window.addEventListener('load', moverIndicador);
  moverIndicador();
})();
