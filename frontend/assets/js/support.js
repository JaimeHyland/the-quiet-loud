/* ============================================
   SUPPORT.JS — Scroll fade observer
   ============================================ */

const observer = new IntersectionObserver(
    (entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) entry.target.classList.add('visible');
        });
    },
    { threshold: 0.12 }
);

document.querySelectorAll('.fade-section').forEach(el => observer.observe(el));