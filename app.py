import streamlit as st
import datetime

st.set_page_config(
    page_title="The Juggling Model | CognitiveCloud.ai",
    page_icon="⚽",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
    background-color: #0a0e1a;
    color: #e8eaf0;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 1.5rem 4rem; max-width: 720px; }

.binary-bg {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: #1a1a2a;
    letter-spacing: 4px;
    text-align: center;
    line-height: 2;
    margin-bottom: -1.5rem;
    animation: pulse 4s ease-in-out infinite;
}
@keyframes pulse { 0%,100%{opacity:0.3} 50%{opacity:0.6} }

.site-label {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 4px;
    color: #4ade80;
    text-transform: uppercase;
    text-align: center;
    margin-bottom: 0.25rem;
}
.main-title {
    font-size: 2.8rem;
    font-weight: 700;
    text-align: center;
    color: #ffffff;
    line-height: 1.1;
    margin-bottom: 0.25rem;
}
.main-title span { color: #f59e0b; }
.subtitle {
    text-align: center;
    font-size: 0.95rem;
    color: #7a8399;
    letter-spacing: 1px;
    margin-bottom: 2rem;
}
.badge {
    display: inline-block;
    background: #111827;
    border: 1px solid #2a3a2a;
    border-radius: 999px;
    padding: 0.3rem 1.1rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    color: #4ade80;
    letter-spacing: 2px;
    margin-bottom: 2rem;
}
.card {
    background: #111827;
    border: 1px solid #1e2d3d;
    border-radius: 16px;
    padding: 1.8rem 2rem;
    margin-bottom: 1.5rem;
}
.card-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 3px;
    color: #f59e0b;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
}
.card h3 { font-size: 1.25rem; font-weight: 600; color: #ffffff; margin-bottom: 0.5rem; }
.card p  { color: #9aa5b8; font-size: 0.95rem; line-height: 1.7; }
.divider { border: none; border-top: 1px solid #1e2d3d; margin: 2rem 0; }
.quote-block {
    border-left: 3px solid #f59e0b;
    padding: 0.8rem 1.2rem;
    background: #0d1117;
    border-radius: 0 10px 10px 0;
    margin: 1rem 0;
}
.quote-block p { color: #f59e0b; font-size: 0.95rem; font-style: italic; margin: 0; }
.resource-item {
    background: #0d1117;
    border: 1px solid #1e2d3d;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.75rem;
}
.resource-title { font-size: 0.9rem; font-weight: 600; color: #e8eaf0; margin-bottom: 0.2rem; }
.resource-meta  { font-family: 'Space Mono', monospace; font-size: 0.65rem; color: #f59e0b; letter-spacing: 2px; }
.resource-desc  { font-size: 0.82rem; color: #7a8399; margin-top: 0.3rem; line-height: 1.5; }
.stButton > button {
    background: #f59e0b !important;
    color: #0a0e1a !important;
    border: none !important;
    border-radius: 999px !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.75rem !important;
    letter-spacing: 2px !important;
    padding: 0.6rem 2rem !important;
    font-weight: 700 !important;
}
.stButton > button:hover { background: #fbbf24 !important; }
.stTextArea textarea {
    background: #0d1117 !important;
    border: 1px solid #1e2d3d !important;
    color: #e8eaf0 !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "persist_log" not in st.session_state:
    st.session_state.persist_log = []

# ── HEADER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="binary-bg">
01110000 01100101 01110010 01110011 01101001 01110011 01110100<br>
00000001 00000000 00000001 00000001 00000000 00000001 00000000<br>
01110010 01100101 01110011 01100101 01110100 00100000 01110100
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="site-label">COGNITIVECLOUD.AI</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; font-family:\'Space Grotesk\',sans-serif; font-size:1.05rem; font-weight:600; color:#4ade80; letter-spacing:1px; margin-bottom:0.15rem;">Positive Mindset Growth Mindset Math</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; font-family:\'Space Mono\',monospace; font-size:0.7rem; color:#4a5568; letter-spacing:3px; margin-bottom:1rem;">COMMON CORE · GRADE 8 · 8.NS · PERSISTENCE</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">THE JUGGLING<span> MODEL</span></div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Plan. Execute. Reset. Never stop.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center"><span class="badge">8.NS · MATHEMATICAL PRACTICE · MP1 + MP6</span></div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# CONCEPT — THE TWO MODELS
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="card">
    <div class="card-label">The Concept · Plan vs. React</div>
    <h3>Where does your mind go when it gets hard?</h3>
    <p>
        A free climber on a cliff doesn't look at where his hand <em>is</em> —
        he plans where it's <em>going</em>. One wrong reaction and he falls.
        Planning is the only move that keeps him on the wall.<br><br>
        A soccer player juggling a ball doesn't chase where it <em>landed</em> —
        she places her foot where it <em>will be</em>. React every time and you
        lose the ball. Anticipate and you stay in control.<br><br>
        <strong style="color:#f59e0b">This is persistence.</strong>
        Not grinding through chaos — but planning your next move
        before the last one finishes.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="quote-block">
    <p>"π never terminates. It never repeats. It just keeps going — and so do you."</p>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# INTERACTIVE — JUGGLING SIMULATION
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown("""
<div class="card">
    <div class="card-label">Interactive · The Juggling Sim</div>
    <h3>Plan your touch. Don't chase the ball.</h3>
    <p>
        The ball will fall. Click <strong style="color:#f59e0b">where you predict it will land</strong>
        before it gets there — not where it is right now.
        Every drop is a reset, not a failure.
        Your persistence score builds across attempts.
    </p>
</div>
""", unsafe_allow_html=True)

st.components.v1.html("""
<!DOCTYPE html>
<html>
<head>
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  html, body { background: transparent; font-family: 'Space Grotesk', 'Segoe UI', sans-serif; overflow: hidden; }

  #canvas-wrap {
    position: relative;
    width: 100%;
    height: 340px;
    background: #0d1117;
    border-radius: 14px;
    border: 1px solid #1e2d3d;
    overflow: hidden;
    cursor: crosshair;
  }

  canvas { display: block; width: 100%; height: 100%; }

  #hud {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 16px;
    background: #111827;
    border-radius: 0 0 14px 14px;
    border: 1px solid #1e2d3d;
    border-top: none;
    margin-bottom: 14px;
  }

  .hud-stat { text-align: center; }
  .hud-val  { font-family: 'Space Mono', monospace; font-size: 1.4rem; font-weight: 700; color: #f59e0b; }
  .hud-lbl  { font-family: 'Space Mono', monospace; font-size: 0.6rem; letter-spacing: 2px; color: #4a5568; }

  #message {
    text-align: center;
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 2px;
    color: #4ade80;
    min-height: 22px;
    margin-bottom: 10px;
    transition: opacity 0.3s;
  }

  .btn-row { display: flex; gap: 10px; justify-content: center; margin-top: 4px; }
  .sim-btn {
    background: #f59e0b;
    color: #0a0e1a;
    border: none;
    border-radius: 999px;
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 2px;
    font-weight: 700;
    padding: 8px 22px;
    cursor: pointer;
    transition: background 0.2s;
  }
  .sim-btn:hover { background: #fbbf24; }
  .sim-btn.secondary {
    background: transparent;
    border: 1px solid #1e2d3d;
    color: #7a8399;
  }
  .sim-btn.secondary:hover { border-color: #f59e0b; color: #f59e0b; }

  #persist-bar-wrap {
    margin: 12px 0 4px;
    background: #1a2233;
    border-radius: 999px;
    height: 8px;
    overflow: hidden;
  }
  #persist-bar {
    height: 100%;
    background: linear-gradient(90deg, #f59e0b, #fbbf24);
    border-radius: 999px;
    width: 0%;
    transition: width 0.5s ease;
  }
  .bar-labels {
    display: flex;
    justify-content: space-between;
    font-family: 'Space Mono', monospace;
    font-size: 0.6rem;
    color: #4a5568;
    letter-spacing: 1px;
    margin-top: 4px;
    margin-bottom: 10px;
  }
</style>
</head>
<body>

<div id="canvas-wrap">
  <canvas id="jcanvas"></canvas>
</div>
<div id="hud">
  <div class="hud-stat"><div class="hud-val" id="hud-touches">0</div><div class="hud-lbl">TOUCHES</div></div>
  <div class="hud-stat"><div class="hud-val" id="hud-planned">0</div><div class="hud-lbl">PLANNED</div></div>
  <div class="hud-stat"><div class="hud-val" id="hud-resets">0</div><div class="hud-lbl">RESETS</div></div>
  <div class="hud-stat"><div class="hud-val" id="hud-persist">0%</div><div class="hud-lbl">PERSISTENCE</div></div>
</div>

<div id="persist-bar-wrap"><div id="persist-bar"></div></div>
<div class="bar-labels"><span>REACTING</span><span>PLANNING</span></div>

<div id="message">CLICK WHERE THE BALL WILL LAND · NOT WHERE IT IS</div>

<div class="btn-row">
  <button class="sim-btn" onclick="startSim()">▶ START</button>
  <button class="sim-btn secondary" onclick="resetSim()">↺ RESET</button>
</div>

<script>
const canvas = document.getElementById('jcanvas');
const ctx = canvas.getContext('2d');
const wrap = document.getElementById('canvas-wrap');

// resize canvas to container
function resize() {
  canvas.width = wrap.clientWidth;
  canvas.height = wrap.clientHeight;
}
resize();
window.addEventListener('resize', resize);

// ── State ──
let running = false;
let ball = { x: 0, y: 0, vx: 0, vy: 0, r: 14 };
let target = null;        // where student clicked
let targetFlash = 0;
let ballHit = false;  // true = planned touch (green flash), false = normal
let ballDrop = false; // true = just dropped (red)
let touches = 0, planned = 0, resets = 0;
let frameId = null;
const GRAVITY = 0.32;
const BOUNCE  = 0.58;
const SPEED   = 2.8;
const HIT_DIST = 44;      // radius to count as planned
const PLAN_WINDOW = 60;   // frames ahead — if click is predictive

// ── Init ball ──
function initBall() {
  ball.x  = canvas.width / 2;
  ball.y  = 60;
  ball.vx = (Math.random() - 0.5) * SPEED * 2;
  ball.vy = 1;
}

// ── Start ──
function startSim() {
  if (running) return;
  running = true;
  initBall();
  setMsg('PLAN YOUR TOUCH · CLICK AHEAD OF THE BALL');
  loop();
}

// ── Reset ──
function resetSim() {
  running = false;
  cancelAnimationFrame(frameId);
  touches = 0; planned = 0; resets = 0;
  target = null;
  updateHUD();
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  setMsg('CLICK WHERE THE BALL WILL LAND · NOT WHERE IT IS');
}

// ── Click ──
wrap.addEventListener('click', (e) => {
  if (!running) return;
  const rect = wrap.getBoundingClientRect();
  const scaleX = canvas.width  / rect.width;
  const scaleY = canvas.height / rect.height;
  target = {
    x: (e.clientX - rect.left)  * scaleX,
    y: (e.clientY - rect.top)   * scaleY,
    age: 0
  };
});

// ── Main loop ──
function loop() {
  if (!running) return;
  update();
  draw();
  frameId = requestAnimationFrame(loop);
}

function update() {
  // physics
  ball.vy += GRAVITY;
  ball.x  += ball.vx;
  ball.y  += ball.vy;

  // wall bounce
  if (ball.x - ball.r < 0) { ball.x = ball.r; ball.vx = Math.abs(ball.vx); }
  if (ball.x + ball.r > canvas.width) { ball.x = canvas.width - ball.r; ball.vx = -Math.abs(ball.vx); }

  // floor — count as reset (drop)
  if (ball.y + ball.r > canvas.height - 8) {
    resets++;
    touches++;
    setMsg('DROP → RESET · PLAN YOUR NEXT TOUCH', '#ef4444');
    setTimeout(() => setMsg('PLAN YOUR TOUCH · CLICK AHEAD'), 900);
    ball.y  = canvas.height - 8 - ball.r;
    ball.vy = -Math.abs(ball.vy) * BOUNCE;
    ball.vx += (Math.random() - 0.5) * 1.2;
    updateHUD();
  }

  // check if target predicts the ball
  if (target) {
    target.age++;
    const dist = Math.hypot(ball.x - target.x, ball.y - target.y);
    if (dist < HIT_DIST && target.age > 8) {
      planned++;
      touches++;
      targetFlash = 18;
      target = null;
      ballHit = true;
      setTimeout(() => { ballHit = false; }, 400);
      setMsg('PLANNED TOUCH ✓', '#4ade80');
      setTimeout(() => setMsg('PLAN YOUR NEXT TOUCH · CLICK AHEAD'), 700);
      // give the ball a controlled kick upward
      ball.vy = -8 - Math.random() * 3;
      ball.vx += (Math.random() - 0.5) * 1.5;
      updateHUD();
    }
    if (target && target.age > 120) target = null; // expire old clicks
  }

  if (targetFlash > 0) targetFlash--;
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // floor line
  ctx.strokeStyle = '#1e2d3d';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(0, canvas.height - 8);
  ctx.lineTo(canvas.width, canvas.height - 8);
  ctx.stroke();

  // ball shadow
  ctx.beginPath();
  ctx.ellipse(ball.x, canvas.height - 8, ball.r * 0.9, 4, 0, 0, Math.PI * 2);
  ctx.fillStyle = ballDrop ? 'rgba(239,68,68,0.2)' : 'rgba(74,222,128,0.18)';
  ctx.fill();

  // ball trajectory ghost (anticipation guide)
  let gx = ball.x, gy = ball.y, gvx = ball.vx, gvy = ball.vy;
  for (let i = 0; i < 28; i++) {
    gvy += GRAVITY;
    gx  += gvx;
    gy  += gvy;
    if (gx < ball.r || gx > canvas.width - ball.r) gvx *= -1;
    if (gy > canvas.height - 8) break;
    const alpha = (1 - i / 28) * 0.25;
    ctx.beginPath();
    ctx.arc(gx, gy, 3, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(74,222,128,${alpha})`;
    ctx.fill();
  }

  // target marker
  if (target) {
    const age = target.age;
    const pulse = Math.sin(age * 0.3) * 4;
    ctx.beginPath();
    ctx.arc(target.x, target.y, 18 + pulse, 0, Math.PI * 2);
    ctx.strokeStyle = targetFlash > 0 ? '#4ade80' : '#f59e0b';
    ctx.lineWidth = 2;
    ctx.setLineDash([4, 4]);
    ctx.stroke();
    ctx.setLineDash([]);
    // crosshair
    ctx.strokeStyle = targetFlash > 0 ? '#4ade80' : '#f59e0b66';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(target.x - 10, target.y);
    ctx.lineTo(target.x + 10, target.y);
    ctx.moveTo(target.x, target.y - 10);
    ctx.lineTo(target.x, target.y + 10);
    ctx.stroke();
  }

  // hit flash ring
  if (targetFlash > 0) {
    const r = (18 - targetFlash) * 2.5;
    ctx.beginPath();
    ctx.arc(ball.x, ball.y, r, 0, Math.PI * 2);
    ctx.strokeStyle = `rgba(74,222,128,${targetFlash / 18})`;
    ctx.lineWidth = 2;
    ctx.stroke();
  }

  // ball — green (ready/planned), red (drop/react)
  const ballColor1 = ballDrop ? '#FCA5A5' : (ballHit ? '#86efac' : '#86efac');
  const ballColor2 = ballDrop ? '#EF4444' : (ballHit ? '#4ade80' : '#4ade80');
  const ballShadow = ballDrop ? 'rgba(239,68,68,0.5)' : 'rgba(74,222,128,0.4)';
  const grad = ctx.createRadialGradient(ball.x - 4, ball.y - 4, 2, ball.x, ball.y, ball.r);
  grad.addColorStop(0, ballColor1);
  grad.addColorStop(1, ballColor2);
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, ball.r, 0, Math.PI * 2);
  ctx.fillStyle = grad;
  ctx.shadowColor = ballShadow;
  ctx.shadowBlur = 14;
  ctx.fill();
  ctx.shadowBlur = 0;

  // soccer lines on ball
  ctx.strokeStyle = 'rgba(0,0,0,0.2)';
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, ball.r * 0.55, 0, Math.PI * 2);
  ctx.stroke();
}

function updateHUD() {
  document.getElementById('hud-touches').textContent = touches;
  document.getElementById('hud-planned').textContent = planned;
  document.getElementById('hud-resets').textContent  = resets;
  const pct = touches > 0 ? Math.round((planned / touches) * 100) : 0;
  document.getElementById('hud-persist').textContent = pct + '%';
  document.getElementById('persist-bar').style.width = pct + '%';
}

function setMsg(txt, color) {
  const el = document.getElementById('message');
  el.textContent = txt;
  el.style.color  = color || '#4ade80';
}
</script>
</body>
</html>
""", height=560, scrolling=False)

# ═══════════════════════════════════════════════════════════════════════════════
# MATH BRIDGE — 8.NS PERSISTENCE
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown("""
<div class="card">
    <div class="card-label">Math Bridge · 8.NS + Persistence</div>
    <h3>Irrational numbers never quit. Neither do you.</h3>
    <p>
        An irrational number like π or √2 never terminates — it keeps going, digit after digit,
        never repeating, never stopping. You can't know it exactly, but you can
        <strong style="color:#f59e0b">approximate it</strong> — plan where it is on the number line
        and get closer with every attempt.<br><br>
        That's the juggling model in math:
    </p>
</div>
""", unsafe_allow_html=True)

st.components.v1.html("""
<!DOCTYPE html>
<html>
<head>
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  html, body { background: transparent; overflow: hidden; font-family: 'Space Grotesk','Segoe UI',sans-serif; }

  .wrapper { padding: 4px; }

  .number-line-wrap {
    background: #0d1117;
    border: 1px solid #1e2d3d;
    border-radius: 14px;
    padding: 24px 28px 20px;
    margin-bottom: 12px;
  }

  .nl-title {
    font-family: monospace;
    font-size: 0.65rem;
    letter-spacing: 3px;
    color: #f59e0b;
    text-transform: uppercase;
    margin-bottom: 16px;
  }

  .line-track {
    position: relative;
    height: 4px;
    background: #1e2d3d;
    border-radius: 999px;
    margin: 32px 0 12px;
  }

  .line-fill {
    height: 100%;
    background: linear-gradient(90deg, #1e3a2a, #f59e0b);
    border-radius: 999px;
    transition: width 0.7s cubic-bezier(.34,1.56,.64,1);
  }

  .tick {
    position: absolute;
    top: -20px;
    transform: translateX(-50%);
    font-family: monospace;
    font-size: 0.7rem;
    color: #4a5568;
  }
  .tick-line {
    position: absolute;
    top: -8px;
    width: 1px;
    height: 20px;
    background: #2a3a4a;
    transform: translateX(-50%);
  }
  .target-tick {
    position: absolute;
    top: -28px;
    transform: translateX(-50%);
    font-family: monospace;
    font-size: 0.75rem;
    font-weight: 700;
    color: #f59e0b;
    white-space: nowrap;
  }
  .approx-dot {
    position: absolute;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 14px; height: 14px;
    border-radius: 50%;
    background: #f59e0b;
    box-shadow: 0 0 10px rgba(245,158,11,0.6);
    transition: left 0.7s cubic-bezier(.34,1.56,.64,1);
  }

  .nl-labels {
    display: flex;
    justify-content: space-between;
    font-family: monospace;
    font-size: 0.65rem;
    color: #4a5568;
    letter-spacing: 1px;
    margin-top: 6px;
  }

  .approx-display {
    text-align: center;
    margin-top: 16px;
    font-family: monospace;
    font-size: 1rem;
    color: #e8eaf0;
    letter-spacing: 2px;
    min-height: 24px;
  }
  .approx-display span { color: #f59e0b; }

  .btn-row {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 14px;
  }
  .nl-btn {
    background: #111827;
    border: 1px solid #1e2d3d;
    color: #9aa5b8;
    font-size: 0.7rem;
    font-family: monospace;
    letter-spacing: 1px;
    padding: 6px 14px;
    border-radius: 999px;
    cursor: pointer;
    transition: all 0.2s;
  }
  .nl-btn:hover, .nl-btn.active { border-color: #f59e0b; color: #f59e0b; background: #1a1500; }

  .insight-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 4px;
  }
  .insight-card {
    background: #0d1117;
    border: 1px solid #1e2d3d;
    border-radius: 10px;
    padding: 14px;
  }
  .ic-label { font-family: monospace; font-size: 0.6rem; letter-spacing: 2px; color: #f59e0b; margin-bottom: 6px; }
  .ic-text  { font-size: 0.8rem; color: #9aa5b8; line-height: 1.6; }
  .ic-text strong { color: #f59e0b; }
</style>
</head>
<body>
<div class="wrapper">

  <div class="number-line-wrap">
    <div class="nl-title">Approximate · Plan Your Position · 8.NS</div>
    <div class="line-track" id="lineTrack">
      <div class="line-fill" id="lineFill" style="width:0%"></div>
      <div class="approx-dot" id="approxDot" style="left:0%"></div>
    </div>
    <div class="nl-labels"><span>1</span><span>1.2</span><span>1.4</span><span>√2 ≈ 1.414</span><span>1.6</span><span>1.8</span><span>2</span></div>

    <div class="approx-display" id="approxDisplay">Select an approximation below</div>

    <div class="btn-row">
      <button class="nl-btn" onclick="setApprox('1.0',  0)">1.0</button>
      <button class="nl-btn" onclick="setApprox('1.2', 20)">1.2</button>
      <button class="nl-btn" onclick="setApprox('1.4', 40)">1.4</button>
      <button class="nl-btn" onclick="setApprox('1.41', 41)">1.41</button>
      <button class="nl-btn" onclick="setApprox('1.414', 41.4)">1.414</button>
      <button class="nl-btn" onclick="setApprox('1.4142', 41.42)">1.4142</button>
      <button class="nl-btn" onclick="setApprox('2.0', 100)">2.0</button>
    </div>
  </div>

  <div class="insight-row">
    <div class="insight-card">
      <div class="ic-label">THE JUGGLER</div>
      <div class="ic-text">Every touch gets the ball closer to <strong>control</strong>. A drop is data — reset and plan the next touch better.</div>
    </div>
    <div class="insight-card">
      <div class="ic-label">THE MATHEMATICIAN</div>
      <div class="ic-text">Every digit gets you closer to <strong>√2</strong>. You never land exactly — but each approximation is a planned touch.</div>
    </div>
  </div>

</div>

<script>
  const TRUE_VAL = 41.42; // √2 mapped to 0–100 scale (1 to 2)

  function setApprox(label, pct) {
    document.getElementById('lineFill').style.width   = pct + '%';
    document.getElementById('approxDot').style.left   = pct + '%';

    const diff = Math.abs(pct - TRUE_VAL);
    let msg, color;
    if (diff === 0) {
      msg = '√2 ≈ <span>' + label + '</span> · Exact to 4 decimal places · Persistence pays off';
      color = '#4ade80';
    } else if (diff < 2) {
      msg = '√2 ≈ <span>' + label + '</span> · Very close · One more digit gets you there';
      color = '#f59e0b';
    } else if (diff < 15) {
      msg = '√2 ≈ <span>' + label + '</span> · Getting closer · Keep planning';
      color = '#f59e0b';
    } else {
      msg = '√2 ≈ <span>' + label + '</span> · Far from true value · Plan your next move';
      color = '#7a8399';
    }

    const d = document.getElementById('approxDisplay');
    d.innerHTML = msg;
    d.style.color = color;

    document.querySelectorAll('.nl-btn').forEach(b => b.classList.remove('active'));
    event.target.classList.add('active');
  }
</script>
</body>
</html>
""", height=340, scrolling=False)

# ═══════════════════════════════════════════════════════════════════════════════
# PERSISTENCE CHECK-IN
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown("""
<div class="card">
    <div class="card-label">Persistence Check-In</div>
    <h3>Name your wall.</h3>
    <p>
        Every climber has a move on the wall that stops them.
        Every juggler has a rhythm they haven't found yet.
        What's the 8th grade math concept that feels like your hardest hold?
    </p>
</div>
""", unsafe_allow_html=True)

wall = st.text_area("", placeholder="Write the concept, then write your next planned move — not a reaction.", height=110, key="wall_input", label_visibility="collapsed")

persist_options = [
    "I will attempt it once before asking for help.",
    "I will find one example and work through it slowly.",
    "I will teach the concept to myself out loud.",
    "I will approximate — get close — and refine from there.",
    "I will reset without judgment and plan my next touch.",
]

plan = st.selectbox("Your next planned move:", [""] + persist_options, key="persist_plan")
custom_plan = st.text_input("Or write your own plan:", placeholder="My next planned move is...", key="custom_plan")
final_plan = custom_plan if custom_plan else plan

if final_plan and final_plan != "":
    st.markdown(f"""
    <div style="background:#1a1200; border:1px solid #f59e0b; border-radius:12px; padding:1.2rem 1.5rem; margin:1rem 0;">
        <div style="font-family:'Space Mono',monospace; font-size:0.65rem; color:#f59e0b; letter-spacing:3px; margin-bottom:0.4rem">YOUR NEXT PLANNED TOUCH</div>
        <div style="font-size:1rem; color:#e8eaf0;">⚽ &nbsp;{final_plan}</div>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("LOCK IN MY PLAN →", key="lock_plan"):
        entry = {
            "date": datetime.date.today().strftime("%b %d, %Y"),
            "wall": wall[:80] + "..." if len(wall) > 80 else wall,
            "plan": final_plan,
        }
        st.session_state.persist_log.insert(0, entry)
        st.balloons()
        st.success("✅ Plan locked. Reset. Go again.")

if st.session_state.persist_log:
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<div style="font-family:\'Space Mono\',monospace; font-size:0.7rem; color:#f59e0b; letter-spacing:3px; margin-bottom:1rem;">PERSISTENCE LOG · YOUR PLANNED TOUCHES</div>', unsafe_allow_html=True)
    for entry in st.session_state.persist_log:
        st.markdown(f"""
        <div style="border-left:2px solid #f59e0b; padding:0.6rem 1rem; margin-bottom:0.75rem; background:#0d1117; border-radius:0 8px 8px 0;">
            <div style="font-family:'Space Mono',monospace; font-size:0.65rem; color:#f59e0b; letter-spacing:2px;">{entry['date']}</div>
            {f'<div style="font-size:0.85rem; color:#9aa5b8; margin-top:0.2rem;">Wall: {entry["wall"]}</div>' if entry.get('wall') else ''}
            <div style="font-size:0.85rem; color:#e8eaf0; margin-top:0.2rem;">⚽ {entry['plan']}</div>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# EDUCATOR RESOURCES
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown("""
<div class="card">
    <div class="card-label">Educator Resources · Research</div>
    <h3>Locomotion, Motor Skills & Cognitive Development</h3>
    <p>
        The connection between physical movement, planning, and mathematical thinking
        is well-documented. These resources ground the Juggling Model in research.
    </p>
</div>
""", unsafe_allow_html=True)

resources = [
    {
        "title": "Motor Skill Development and Mathematical Achievement",
        "meta": "JOURNAL OF EDUCATIONAL PSYCHOLOGY · RESEARCH",
        "desc": "Studies show fine and gross motor skill proficiency in early grades is a significant predictor of later mathematical achievement, suggesting shared neural pathways between spatial-motor planning and numerical reasoning.",
        "url": "https://doi.org/10.1037/edu0000660"
    },
    {
        "title": "Embodied Cognition: How Movement Shapes Mathematical Thinking",
        "meta": "COGNITIVE SCIENCE · FOUNDATIONAL THEORY",
        "desc": "Embodied cognition research demonstrates that physical experience — including locomotion and gesture — directly shapes abstract mathematical understanding, including number line estimation and spatial reasoning.",
        "url": "https://www.sciencedirect.com/science/article/pii/S0010027713001704"
    },
    {
        "title": "Anticipatory Motor Planning in Expert Jugglers",
        "meta": "NEUROPSYCHOLOGIA · MOTOR NEUROSCIENCE",
        "desc": "Expert jugglers show heightened predictive brain activity in regions associated with spatial planning and executive function — the same regions activated during complex mathematical problem solving.",
        "url": "https://www.sciencedirect.com/science/article/abs/pii/S0028393209004801"
    },
    {
        "title": "Physical Activity, Executive Function, and Academic Achievement",
        "meta": "BRITISH JOURNAL OF EDUCATIONAL PSYCHOLOGY · META-ANALYSIS",
        "desc": "Meta-analysis of 26 studies finds consistent positive relationships between structured physical activity involving planning (not just aerobic activity) and executive function, which mediates math performance.",
        "url": "https://bpspsychub.onlinelibrary.wiley.com/doi/abs/10.1111/bjep.12355"
    },
    {
        "title": "The Role of Spatial Skills in Mathematics: A Meta-Analytic Review",
        "meta": "PSYCHOLOGICAL BULLETIN · META-ANALYSIS",
        "desc": "Spatial skills — closely linked to locomotor planning and body awareness — are among the strongest predictors of mathematical competence across all grade levels, particularly in number sense and algebra.",
        "url": "https://doi.org/10.1037/bul0000349"
    },
    {
        "title": "Growth Mindset and Persistence in STEM: Longitudinal Evidence",
        "meta": "CHILD DEVELOPMENT · LONGITUDINAL STUDY",
        "desc": "Students with growth mindset who are taught persistence strategies through embodied metaphors (physical challenge + reset framing) show greater gains in math self-efficacy and problem-solving endurance.",
        "url": "https://srcd.onlinelibrary.wiley.com/doi/abs/10.1111/cdev.13527"
    },
]

for r in resources:
    st.markdown(f"""
    <div class="resource-item">
        <div class="resource-title">{r['title']}</div>
        <div class="resource-meta">{r['meta']}</div>
        <div class="resource-desc">{r['desc']}</div>
        <a href="{r['url']}" target="_blank" style="font-family:'Space Mono',monospace; font-size:0.6rem; color:#f59e0b; letter-spacing:2px; text-decoration:none; margin-top:0.4rem; display:inline-block;">VIEW RESEARCH →</a>
    </div>
    """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding:3rem 0 1rem; border-top:1px solid #1e2d3d; margin-top:3rem;">
    <p style="font-family:'Space Mono',monospace; font-size:0.65rem; color:#2a3a2a; letter-spacing:3px;">
        COGNITIVECLOUD.AI · XAVIER HONABLUE M.ED · 8.NS · THE JUGGLING MODEL
    </p>
</div>
""", unsafe_allow_html=True)
