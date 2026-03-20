import codecs

html_path = 'c:/Users/Atharva/OneDrive/Desktop/supply chain risk/chainguard_demo.html'
with codecs.open(html_path, 'r', 'utf-8') as f:
    text = f.read()

nav_inject = """      <div class="nav-item" onclick="nav('scenario',this)"><span class="nav-icon">⚄</span>Scenario Engine</div>
      <div class="nav-item" onclick="nav('india',this)"><span class="nav-icon">🇮🇳</span>India Intelligence</div>
      <div class="nav-item" onclick="nav('alerts',this)"><span class="nav-icon">🔔</span>Smart Alert System</div>"""

if '<div class="nav-item" onclick="nav(\'india\',this)">' not in text:
    text = text.replace(
        '<div class="nav-item" onclick="nav(\'scenario\',this)"><span class="nav-icon">⚄</span>Scenario Engine</div>',
        nav_inject
    )
    
    text = text.replace(
        "scenario: 'What-If Cost Simulation', analytics: 'Analytics & Insights', tracker: '📍 Real-Time Location Tracker' };",
        "scenario: 'What-If Cost Simulation', india: 'India Intelligence & AI Early Warning', alerts: 'Smart Alert System', analytics: 'Analytics & Insights', tracker: '📍 Real-Time Location Tracker' };"
    )
    
    text = text.replace(
        "if (page === 'scenario') loadScenario();",
        "if (page === 'scenario') loadScenario();\n      if (page === 'india') loadIndia();\n      if (page === 'alerts') loadAlerts();"
    )

pages_html = """
    <!-- INDIA INTELLIGENCE -->
    <div class="page" id="page-india">
      <div class="g46" style="align-items:start">
        <div class="card">
          <div class="ch">
            <div>
              <div class="ct">India-Specific Risk & AI Early Warning</div>
              <div class="csub">Predict disruption 7–30 days early based on local telemetry</div>
            </div>
          </div>
          
          <div class="stats" style="grid-template-columns: 1fr 1fr;">
            <div class="scard w" style="padding:14px;">
              <div class="slabel">Monsoon Risk (Next 14 Days)</div>
              <div class="sval">Severe</div>
              <div class="ssub up">Red Alert: Maharashtra coast</div>
            </div>
            <div class="scard d" style="padding:14px;">
              <div class="slabel">Port Delay Prediction</div>
              <div class="sval">+6 Days</div>
              <div class="ssub up" style="color:var(--danger)">JNPT & Mundra capacity at 98%</div>
            </div>
          </div>
          <div class="stats" style="grid-template-columns: 1fr 1fr; margin-bottom:18px;">
            <div class="scard i" style="padding:14px;">
              <div class="slabel">Festival Demand Spike</div>
              <div class="sval">Diwali Peak</div>
              <div class="ssub">+45% projected logistics constraint</div>
            </div>
            <div class="scard s" style="padding:14px;">
              <div class="slabel">Highway Congestion Risk</div>
              <div class="sval">NH-48 Alert</div>
              <div class="ssub up" style="color:var(--danger)">Toll delays expect +4hrs</div>
            </div>
          </div>
          
          <div class="ct" style="font-size:12.5px;margin-bottom:12px">AI 30-Day Disruption Probability Forecast</div>
          <div style="position: relative; height: 180px; width: 100%;"><canvas id="indiaAiChart"></canvas></div>
        </div>
        
        <div class="card">
          <div class="ch">
            <div>
              <div class="ct">AI Early Warning Feed</div>
              <div class="csub">7-30 Day Outlook Insights</div>
            </div>
          </div>
          
          <div class="tl">
            <div class="tli"><div class="tldot" style="background:var(--danger)"></div>
            <div><div class="tltitle">Monsoon Flooding Risk - Mumbai Logistics Hub</div><div class="tlmeta"><span>Lead Time: 8 Days</span><span>Probability: 86%</span><span style="color:var(--danger)">High Impact</span></div></div></div>
            
            <div class="tli"><div class="tldot" style="background:var(--warning)"></div>
            <div><div class="tltitle">Diwali Logistics Capacity Crunch</div><div class="tlmeta"><span>Lead Time: 28 Days</span><span>Probability: 95%</span><span style="color:var(--warning)">Medium Impact</span></div></div></div>
            
            <div class="tli"><div class="tldot" style="background:var(--danger)"></div>
            <div><div class="tltitle">JNPT Port Berth Congestion Spillover</div><div class="tlmeta"><span>Lead Time: 12 Days</span><span>Probability: 78%</span><span style="color:var(--danger)">High Impact</span></div></div></div>
            
            <div class="tli"><div class="tldot" style="background:var(--info)"></div>
            <div><div class="tltitle">NH-48 Toll Infrastructure Maintenance</div><div class="tlmeta"><span>Lead Time: 15 Days</span><span>Probability: 62%</span><span style="color:var(--info)">Low Impact</span></div></div></div>
          </div>
        </div>
      </div>
    </div>

    <!-- SMART ALERTS -->
    <div class="page" id="page-alerts">
      <div class="g64" style="align-items:start">
        <div class="card">
          <div class="ch">
            <div>
              <div class="ct">Smart Alert Control Center</div>
              <div class="csub">Configure multichannel disruption notifications</div>
            </div>
          </div>
          
          <div class="fgrid">
            <div class="fg" style="margin-bottom:15px">
              <label class="fl" style="font-size:14px;color:var(--text);margin-bottom:8px">1. Select Threat Trigger</label>
              <select class="ai-input" id="alertTrigger">
                <option>Risk Index > 75% (Critical)</option>
                <option>Supplier ML Failure Probability > 80%</option>
                <option>Delivery Delay > 48 Hours</option>
                <option>Monsoon / Extreme Weather Alert</option>
              </select>
            </div>
            
            <div class="fg" style="margin-bottom:15px">
              <label class="fl" style="font-size:14px;color:var(--text);margin-bottom:8px">2. Select Notification Channels</label>
              <div style="display:flex;gap:15px;align-items:center;">
                <label style="cursor:pointer; display:flex; align-items:center; gap:5px;"><input type="checkbox" checked id="chkDash"> Dashboard Banner</label>
                <label style="cursor:pointer; display:flex; align-items:center; gap:5px;"><input type="checkbox" checked id="chkEmail"> Email</label>
                <label style="cursor:pointer; display:flex; align-items:center; gap:5px;"><input type="checkbox" checked id="chkSms"> SMS / WhatsApp</label>
              </div>
            </div>
            
            <div class="fg">
              <label class="fl" style="font-size:14px;color:var(--text);margin-bottom:8px">3. Recipient Information</label>
              <input type="text" class="ai-input" id="alertContact" placeholder="manager@supply.in, +91 9876543210" value="procurement_team@chainguard.in">
            </div>
          </div>
          
          <div style="margin-top:25px;display:flex;gap:12px;align-items:center">
            <button class="btn" onclick="fireTestAlert()" style="background:linear-gradient(135deg, #EF4444, #B91C1C)">🔔 Trigger Test Alert</button>
            <span style="font-size:11.5px;color:var(--text-dim)" id="alertFeedback"></span>
          </div>
        </div>
        
        <div class="card">
          <div class="ch">
            <div>
              <div class="ct">Active System Alerts</div>
              <div class="csub">Global Dashboard Notification Stream</div>
            </div>
          </div>
          
          <div id="dashboardAlertStream">
            <div class="alert"><div class="pulse-dot" style="animation:none;background:var(--warning)"></div><div><strong>Auto-Alert System Online</strong><br><span style="color:var(--text-dim);font-size:11px;">Waiting for triggers...</span></div></div>
          </div>
        </div>
      </div>
    </div>
"""

if 'id="page-india"' not in text:
    text = text.replace(
        "    <!-- ANALYTICS -->",
        pages_html + "\n    <!-- ANALYTICS -->"
    )

js_inject = """
    function loadIndia() {
      if(!ch['indiaAi']) {
        const ctx = document.getElementById('indiaAiChart').getContext('2d');
        const g = ctx.createLinearGradient(0, 0, 0, 180);
        g.addColorStop(0, 'rgba(239,68,68,.3)'); g.addColorStop(1, 'rgba(239,68,68,0)');
        
        const dates = [];
        const probs = [];
        let p = 30;
        for(let i=1; i<=30; i++) {
          dates.push('Day +' + i);
          p += (Math.random()-0.4)*8; // slight upward trend
          p = Math.max(10, Math.min(98, p));
          if(i>24) p += 15; // Spike around end of 30 days due to festival/monsoon projection
          p = Math.min(99, p);
          probs.push(p.toFixed(1));
        }
        
        ch['indiaAi'] = new Chart(ctx, {
          type: 'line', data: { labels: dates, datasets: [{ data: probs, borderColor: '#EF4444', backgroundColor: g, borderWidth: 2, fill: true, tension: .4 }] },
          options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { x: { ticks: { maxTicksLimit: 6 }, grid: { display: false } }, y: { min: 0, max: 100, ticks: { callback: v => v + '%' } } } }
        });
      }
    }

    function loadAlerts() {
       // Intentionally empty init
    }
    
    function fireTestAlert() {
       const trigger = document.getElementById('alertTrigger').value;
       const dash = document.getElementById('chkDash').checked;
       const email = document.getElementById('chkEmail').checked;
       const sms = document.getElementById('chkSms').checked;
       const contact = document.getElementById('alertContact').value;
       
       const btn = document.querySelector('button[onclick="fireTestAlert()"]');
       const fb = document.getElementById('alertFeedback');
       
       btn.textContent = "Sending...";
       fb.textContent = "";
       
       setTimeout(() => {
           let msg = "";
           if(email) msg += "[Email Sent] ";
           if(sms) msg += "[SMS Dispatched] ";
           fb.innerHTML = `<span style="color:var(--success)">✓ ${msg} to ${contact}</span>`;
           btn.textContent = "🔔 Trigger Test Alert";
           
           if(dash) {
               const stream = document.getElementById('dashboardAlertStream');
               const d = new Date().toLocaleTimeString();
               const div = document.createElement('div');
               div.className = 'alert';
               div.style.background = 'rgba(239, 68, 68, .08)';
               div.style.borderColor = 'rgba(239, 68, 68, .3)';
               div.style.color = '#FCA5A5';
               div.innerHTML = `<div class="pulse-dot"></div><div><strong>[TEST ALERT] ${trigger}</strong><br><span style="color:var(--text-dim);font-size:11px;">Triggered manually at ${d}</span></div>`;
               stream.insertBefore(div, stream.firstChild);
           }
       }, 800);
    }
"""

if 'function loadIndia()' not in text:
    text = text.replace(
        "// ── ANALYTICS ──",
        js_inject + "\n    // ── ANALYTICS ──"
    )

with codecs.open(html_path, 'w', 'utf-8') as f:
    f.write(text)
print("Injected India Intelligence and Alert Systems")
