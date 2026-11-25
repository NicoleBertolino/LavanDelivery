// Carrossel "Como funciona" da página inicial.
(function () {
  const carousel = document.getElementById('how-carousel');
  if (!carousel) return;

  const track = document.getElementById('how-track');
  const dots = carousel.querySelectorAll('.dot');
  const slides = track.querySelectorAll('.carousel-slide');
  let atual = 0;
  let timer = null;

  function ir(n) {
    atual = (n + slides.length) % slides.length;
    track.style.transform = 'translateX(-' + (atual * 100) + '%)';
    dots.forEach(function (d, i) { d.classList.toggle('active', i === atual); });
  }

  function iniciarAuto() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    pararAuto();
    timer = setInterval(function () { ir(atual + 1); }, 4200);
  }

  function pararAuto() { clearInterval(timer); }

  document.getElementById('how-prev').addEventListener('click', function () { pararAuto(); ir(atual - 1); iniciarAuto(); });
  document.getElementById('how-next').addEventListener('click', function () { pararAuto(); ir(atual + 1); iniciarAuto(); });
  dots.forEach(function (d) {
    d.addEventListener('click', function () { pararAuto(); ir(Number(d.dataset.i)); iniciarAuto(); });
  });
  carousel.addEventListener('mouseenter', pararAuto);
  carousel.addEventListener('mouseleave', iniciarAuto);

  iniciarAuto();
})();
