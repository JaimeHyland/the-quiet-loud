/* ============================================
   HOME.JS — index.html scroll animations
   ============================================ */

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
            setTimeout(() => entry.target.classList.add('visible'), i * 120);
        }
    });
}, { threshold: 0.15 });

document.querySelectorAll('.step, .promise-item').forEach(el => observer.observe(el));