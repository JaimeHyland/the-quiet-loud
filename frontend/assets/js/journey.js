/* ============================================
   JOURNEY.JS — Journey page logic
   ============================================ */
alert("JOURNEY JS SCRIPT")
const emotionMap = {
    joy: { icon: '☀️', label: 'Joy' },
    love: { icon: '🤍', label: 'Love' },
    sad: { icon: '🌧️', label: 'Sad' },
    anger: { icon: '🔥', label: 'Anger' },
    fear: { icon: '🌑', label: 'Fear' },
    surprise: { icon: '✨', label: 'Surprise' }
};

const habitLabels = {
    sleep: '🌙 Sleep',
    move: '🏃 Moved',
    outside: '🌿 Outside',
    connect: '🤝 Connected',
    water: '💧 Hydrated',
    screen: '📵 Screen break'
};

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

async function loadEntries() {
    console.log("INVOKING LOAD ENTRIES, FETCHING NOW")
    try {
        const res = await fetch('/mood/logged-emotions/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            credentials: "include"
        });
        const data = await res.json();
        console.log("DATA: ", data)
        renderEntries(data);
    } catch (e) {
        console.error('Getting user emotions failed', e);
        renderEntries([]);
    }
}

// ── RENDER ENTRIES ──
function renderEntries(entries) {
    // console.log("ENTRIES: ", entries)
    const container = document.getElementById('entriesList');
    if (!container) return;

    if (!entries || entries.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <div class="empty-state-icon">🌿</div>
                <p>Your journey hasn't started yet.<br>Write your first entry today.</p>
                <a href="/today/" class="btn-start">Begin today</a>
            </div>`;
        return;
    }

    const chartNote = document.getElementById('chartNote');
    if (chartNote) chartNote.style.display = 'none';

    container.innerHTML = entries.user_emotions.map(entry => {
        const date = new Date(entry.date || entry.created_at);
        const dateStr = date.toLocaleDateString('en-GB', {
            weekday: 'long', day: 'numeric', month: 'long'
        });


        const emotion = entry.predicted_emotion
            ? (emotionMap[entry.predicted_emotion] || { icon: '💭', label: entry.predicted_emotion })
            : null;
        const emotionHTML = emotion
            ? `<div class="entry-emotion">${emotion.icon} ${emotion.label}</div>`
            : '';
        const habitsHTML = (entry.habits || [])
            .map(h => `<span class="habit-chip">${habitLabels[h] || h}</span>`)
            .join('');
        const sleepHTML = entry.sleep
            ? `<span class="sleep-chip">🌙 ${entry.sleep}</span>`
            : '';
        const textPreview = entry.user_mood_text
            ? `<p class="entry-text">${entry.user_mood_text.replace(/[\[\],']/g, "")}</p>`
            : '';

        return `
            <div class="entry-card">
                <div class="entry-card-header">
                    <span class="entry-date">${entry.date}</span>
                    ${emotionHTML}
                </div>
                ${textPreview}
                <div class="entry-footer">
                    ${sleepHTML}
                    ${habitsHTML}
                </div>
            </div>`;
    }).join('');
}
loadEntries();