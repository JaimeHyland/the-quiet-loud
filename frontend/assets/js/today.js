/* ============================================
   TODAY.JS — Today page logic
   ============================================ */

// ── SET TODAY'S DATE ──
const dateEl = document.getElementById('todayDate');
if (dateEl) {
    const now = new Date();
    dateEl.textContent = now.toLocaleDateString('en-GB', {
        weekday: 'long', day: 'numeric', month: 'long', year: 'numeric'
    });
}

// ── CHAR COUNTER ──
const freeText = document.getElementById('freeText');
const charCount = document.getElementById('charCount');
const saveBtn = document.getElementById('saveBtn');
const minMsg = document.getElementById('minMsg');

if (freeText) {
    freeText.addEventListener('input', () => {
        const len = freeText.value.length;
        charCount.textContent = len;

        if (len >= 100) {
            saveBtn.disabled = false;
            saveBtn.style.opacity = '1';
            minMsg.style.display = 'none';
        } else {
            saveBtn.disabled = true;
            saveBtn.style.opacity = '0.5';
            minMsg.style.display = 'inline';
            minMsg.textContent = `${100 - len} more characters needed`;
        }
    });
}

// ── HABIT TOGGLES ──
function toggleHabit(el) {
    el.classList.toggle('active');
}

// ── SLEEP SELECTION ──
function selectSleep(el) {
    document.querySelectorAll('.sleep-btn').forEach(b => b.classList.remove('active'));
    el.classList.add('active');
}

// ── EMOTION MAP ──
const emotionMap = {
    joy: { icon: '☀️', label: 'Joy' },
    love: { icon: '🤍', label: 'Love' },
    sad: { icon: '🌧️', label: 'Sad' },
    anger: { icon: '🔥', label: 'Anger' },
    fear: { icon: '🌑', label: 'Fear' },
    surprise: { icon: '✨', label: 'Surprise' }
};

// ── CSRF HELPER ──
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// ── SAVE ENTRY ──
async function saveEntry() {
    const text = document.getElementById('freeText').value;

    try {
        console.log("ATTEMPTING FETCH")
        const res = await fetch('/mood/predict/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            credentials: 'include',
            body: JSON.stringify({
                text: text,
                sleep: document.querySelector('.sleep-btn.active')?.textContent || null,
                gratitude: document.getElementById('gratitudeText').value,
                habits: [...document.querySelectorAll('.habit-toggle.active')].map(h => h.dataset.habit),
            })
        });

        const data = await res.json();

        if (data.redirect_url) {
            window.location.href = data.redirect_url;
        }

        if (data.emotion) {
            const emotion = emotionMap[data.emotion] || { icon: '💭', label: data.emotion };
            document.getElementById('emotionIcon').textContent = emotion.icon;
            document.getElementById('emotionLabel').textContent = emotion.label;
            document.getElementById('emotionResult').style.display = 'block';
        }

    } catch (e) {
        console.error('Save failed', e);
    }

    // Show toast
    const toast = document.getElementById('toast');
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 3000);
}