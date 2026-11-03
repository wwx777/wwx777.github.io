(() => {
  const header = document.querySelector('.site-header');
  const navigation = [...document.querySelectorAll('nav a[href^="#"]')];
  const sections = navigation.map(link => document.querySelector(link.hash)).filter(Boolean);
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let scheduled = false;

  function updateNavigation() {
    header.classList.toggle('is-scrolled', window.scrollY > 8);
    const offset = header.getBoundingClientRect().height + 42;
    let active = sections[0];
    for (const section of sections) {
      if (section.getBoundingClientRect().top <= offset) active = section;
    }
    if (window.scrollY > 0 && window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4) {
      active = sections[sections.length - 1];
    }
    for (const link of navigation) {
      if (active && link.hash === `#${active.id}`) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    }
    scheduled = false;
  }

  window.addEventListener('scroll', () => {
    if (!scheduled) {
      scheduled = true;
      window.requestAnimationFrame(updateNavigation);
    }
  }, { passive: true });
  window.addEventListener('resize', updateNavigation, { passive: true });
  updateNavigation();

  if (!('IntersectionObserver' in window) || reducedMotion.matches) return;

  // Enhance only offscreen sections; visible content never waits for a reveal.
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add('reveal-ready');
      entry.target.classList.remove('reveal-pending');
      observer.unobserve(entry.target);
    }
  }, { threshold: 0, rootMargin: '0px 0px -24px 0px' });

  for (const section of document.querySelectorAll('main > section')) {
    if (section.getBoundingClientRect().top <= window.innerHeight) continue;
    section.classList.add('reveal-pending');
    observer.observe(section);
  }

  reducedMotion.addEventListener('change', event => {
    if (!event.matches) return;
    observer.disconnect();
    for (const section of document.querySelectorAll('.reveal-pending')) {
      section.classList.remove('reveal-pending');
    }
  });
})();
