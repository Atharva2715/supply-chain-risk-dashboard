import os
import re

html_path = 'c:/Users/Atharva/OneDrive/Desktop/supply chain risk/chainguard_demo.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Inject CSS
css_inject = """
    /* AI COPILOT CHAT */
    .ai-btn {
      position: fixed;
      bottom: 24px;
      right: 28px;
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: linear-gradient(135deg, #6366F1, #8B5CF6);
      color: #fff;
      font-size: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 4px 20px rgba(99, 102, 241, 0.4);
      z-index: 999;
      transition: transform 0.2s;
    }
    .ai-btn:hover {
      transform: scale(1.08);
    }
    .ai-panel {
      position: fixed;
      bottom: 90px;
      right: 28px;
      width: 380px;
      height: 520px;
      background: rgba(13, 21, 37, 0.95);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border);
      border-radius: 16px;
      z-index: 998;
      display: flex;
      flex-direction: column;
      box-shadow: 0 10px 40px rgba(0,0,0,0.5);
      opacity: 0;
      pointer-events: none;
      transform: translateY(20px);
      transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
      overflow: hidden;
    }
    .ai-panel.open {
      opacity: 1;
      pointer-events: auto;
      transform: translateY(0);
    }
    .ai-header {
      padding: 16px 20px;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      gap: 12px;
      background: rgba(0,0,0,0.2);
    }
    .ai-icon {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: linear-gradient(135deg, #6366F1, #8B5CF6);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: bold;
      font-family: 'Syne', sans-serif;
    }
    .ai-title {
      font-family: 'Syne', sans-serif;
      font-weight: 700;
      font-size: 15px;
    }
    .ai-status {
      font-size: 11px;
      color: var(--accent);
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .ai-status::before {
      content: '';
      width: 6px;
      height: 6px;
      background: var(--accent);
      border-radius: 50%;
      animation: pulse 2s infinite;
    }
    .ai-body {
      flex: 1;
      padding: 16px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .ai-msg {
      max-width: 85%;
      padding: 12px 16px;
      border-radius: 12px;
      font-size: 13px;
      line-height: 1.5;
    }
    .ai-msg.bot {
      background: var(--surface2);
      align-self: flex-start;
      border-bottom-left-radius: 4px;
      color: var(--text);
    }
    .ai-msg.user {
      background: linear-gradient(135deg, #6366F1, #8B5CF6);
      align-self: flex-end;
      border-bottom-right-radius: 4px;
      color: #fff;
    }
    .ai-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: auto;
      padding-top: 10px;
    }
    .ai-chip {
      background: rgba(99, 102, 241, 0.15);
      border: 1px solid rgba(99, 102, 241, 0.3);
      color: #A5B4FC;
      padding: 6px 12px;
      border-radius: 20px;
      font-size: 11.5px;
      cursor: pointer;
      transition: all 0.2s;
    }
    .ai-chip:hover {
      background: rgba(99, 102, 241, 0.3);
      color: #fff;
    }
    .ai-input-area {
      padding: 14px;
      border-top: 1px solid var(--border);
      display: flex;
      gap: 8px;
      background: rgba(0,0,0,0.2);
    }
    .ai-input {
      flex: 1;
      background: var(--surface);
      border: 1px solid var(--border);
      padding: 10px 14px;
      border-radius: 20px;
      color: var(--text);
      font-family: 'DM Sans', sans-serif;
      font-size: 13px;
      outline: none;
    }
    .ai-input:focus {
      border-color: #6366F1;
    }
    .ai-send {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: var(--surface2);
      border: none;
      color: var(--text);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s;
    }
    .ai-send:hover {
      background: #6366F1;
      color: #fff;
    }
    .typing-dot {
      display: inline-block;
      width: 6px;
      height: 6px;
      background: var(--text-muted);
      border-radius: 50%;
      margin: 0 2px;
      animation: typing 1.4s infinite ease-in-out both;
    }
    .typing-dot:nth-child(1) { animation-delay: -0.32s; }
    .typing-dot:nth-child(2) { animation-delay: -0.16s; }
    @keyframes typing {
      0%, 80%, 100% { transform: scale(0); }
      40% { transform: scale(1); }
    }
"""

# Inject CSS just before </style>
if "/* AI COPILOT CHAT */" not in text:
    text = text.replace("</style>", css_inject + "\n</style>")

# 2. Inject HTML UI
html_inject = """
  <!-- AI COPILOT UI -->
  <div class="ai-btn" onclick="toggleAI()">✨</div>
  <div class="ai-panel" id="aiPanel">
    <div class="ai-header">
      <div class="ai-icon">AI</div>
      <div>
        <div class="ai-title">ChainGuard Copilot</div>
        <div class="ai-status">Online · Ready to assist</div>
      </div>
      <span style="margin-left:auto;cursor:pointer;color:var(--text-dim);font-size:18px;" onclick="toggleAI()">✕</span>
    </div>
    <div class="ai-body" id="aiBody">
      <div class="ai-msg bot">Hello! I am your ChainGuard AI Risk Analyst. I've analyzed your live supply chain network.<br><br>I noticed <strong>18 suppliers</strong> are currently in the high-risk zone. How can I assist you in mitigating these risks today?</div>
      
      <div class="ai-chips">
        <div class="ai-chip" onclick="askCopilot('Summarize highest risk suppliers')">Summarize highest risk risks</div>
        <div class="ai-chip" onclick="askCopilot('Draft mitigation plan for SUP1025')">Draft mitigation for SUP1025</div>
        <div class="ai-chip" onclick="askCopilot('What happens if fuel increases 20%?')">Run fuel shock scenario</div>
      </div>
    </div>
    <div class="ai-input-area">
      <input type="text" class="ai-input" id="aiInput" placeholder="Ask about risks, suppliers, or logistics..." onkeypress="if(event.key==='Enter')sendAI()">
      <button class="ai-send" onclick="sendAI()">➤</button>
    </div>
  </div>
"""
if "<!-- AI COPILOT UI -->" not in text:
    text = text.replace("<!-- SUPPLIER DETAIL MODAL -->", html_inject + "\n  <!-- SUPPLIER DETAIL MODAL -->")

# 3. Inject JS
js_inject = """
    // --- AI COPILOT LOGIC ---
    function toggleAI() {
      document.getElementById('aiPanel').classList.toggle('open');
    }
    
    function appendMsg(text, type='bot') {
      const b = document.getElementById('aiBody');
      const d = document.createElement('div');
      d.className = 'ai-msg ' + type;
      if(text === 'typing') {
        d.id = 'typingIndicator';
        d.innerHTML = '<span class="typing-dot"></span><span class="typing-dot"></span><span class="typing-dot"></span>';
      } else {
        d.innerHTML = text;
      }
      // Insert before chips if they exist
      const chips = document.querySelector('.ai-chips');
      if (chips) {
        b.insertBefore(d, chips);
      } else {
        b.appendChild(d);
      }
      b.scrollTop = b.scrollHeight;
    }
    
    function askCopilot(q) {
      document.getElementById('aiInput').value = q;
      sendAI();
    }
    
    async function sendAI() {
      const inp = document.getElementById('aiInput');
      const q = inp.value.trim();
      if(!q) return;
      inp.value = '';
      
      // Hide chips after first interaction for cleaner look
      const chips = document.querySelector('.ai-chips');
      if(chips) chips.style.display = 'none';
      
      appendMsg(q, 'user');
      appendMsg('typing', 'bot');
      
      try {
        const res = await fetch('/ask_ai', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({query: q})
        });
        const data = await res.json();
        document.getElementById('typingIndicator').remove();
        appendMsg(data.answer, 'bot');
      } catch (err) {
        document.getElementById('typingIndicator').remove();
        appendMsg('⚠️ Connection to AI engine lost. Local fallback engaged: "I suggest prioritizing local inventory buffering while the network connection is restored."', 'bot');
      }
    }
"""
if "// --- AI COPILOT LOGIC ---" not in text:
    text = text.replace("  // INIT", js_inject + "\n  // INIT")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Injected AI Copilot UI successfully.")

