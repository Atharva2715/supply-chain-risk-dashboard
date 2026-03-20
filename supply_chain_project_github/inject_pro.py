import codecs
import textwrap

html_path = 'c:/Users/Atharva/OneDrive/Desktop/supply chain risk/chainguard_demo.html'
with codecs.open(html_path, 'r', 'utf-8') as f:
    text = f.read()

# 1. NAVIGATION LINKS INJECTION
nav_additions = """
      <div class="nav-sec">Enterprise Features</div>
      <div class="nav-item" onclick="nav('cost',this)"><span class="nav-icon">₹</span>Cost Impact Prediction</div>
      <div class="nav-item" onclick="nav('integrations',this)"><span class="nav-icon">🔌</span>API Integration</div>
      <div class="nav-item" onclick="nav('reports',this)"><span class="nav-icon">📄</span>Automated Reports</div>
      <div class="nav-item" onclick="nav('history',this)"><span class="nav-icon">⏳</span>Historical Analytics</div>
"""
if "Enterprise Features" not in text:
    anchor_tracker = """<div class="nav-item" onclick="nav('tracker',this)"><span class="nav-icon">📍</span>Live Tracker<span
          class="tracking-pulse" style="font-size:9px;padding:2px 6px;margin-left:auto">LIVE</span></div>"""
    text = text.replace(anchor_tracker, anchor_tracker + nav_additions)

# 2. TITLE MAP INJECTION
if "cost: 'Cost Impact Prediction'" not in text:
    old_titles = "tracker: '📍 Real-Time Location Tracker' };"
    new_titles = "tracker: '📍 Real-Time Location Tracker', cost: 'Cost Impact & Loss Estimation', integrations: 'API & Data Integrations', reports: 'Automated Reporting Center', history: 'Historical Risk Analytics' };"
    text = text.replace(old_titles, new_titles)

# 3. JS PAGE LOADER INJECTION
if "if (page === 'cost') loadCost();" not in text:
    text = text.replace("if (page === 'tracker') { setTimeout(loadTracker, 80); }",
                        "if (page === 'tracker') { setTimeout(loadTracker, 80); }\n      if (page === 'cost') loadCost();\n      if (page === 'integrations') loadIntegrations();\n      if (page === 'reports') loadReports();\n      if (page === 'history') loadHistory();")

# 4. HTML PAGES INJECTION
pages_to_inject = """
    <!-- COST IMPACT PREDICTION -->
    <div class="page" id="page-cost">
      <div class="g46" style="align-items:start">
        <div class="card">
          <div class="ch">
            <div>
              <div class="ct">Loss Estimation Intelligence</div>
              <div class="csub">Dynamic financial exposure tracking from tracked vulnerabilities</div>
            </div>
          </div>
          
          <div class="stats" style="grid-template-columns: 1fr 1fr;">
            <div class="scard d" style="padding:14px;">
              <div class="slabel">Total Projected Loss (Current Risk)</div>
              <div class="sval">₹142.5L</div>
              <div class="ssub up" style="color:var(--danger)">+12.4% vs last week</div>
            </div>
            <div class="scard i" style="padding:14px;">
              <div class="slabel">Estimated Delay Costs</div>
              <div class="sval">₹18.2L</div>
              <div class="ssub">From port & route congestion</div>
            </div>
          </div>
          
          <div class="ct" style="font-size:12.5px;margin:18px 0 12px">Financial Loss Prediction By Sector</div>
          <div style="position: relative; height: 210px; width: 100%;"><canvas id="costLossChart"></canvas></div>
        </div>
        
        <div class="card">
          <div class="ch">
            <div>
              <div class="ct">Delay Cost Predictor</div>
              <div class="csub">Analyzes transit times against penalty clauses</div>
            </div>
          </div>
          
          <div class="tl">
            <div class="tli"><div class="tldot" style="background:var(--danger)"></div>
            <div><div class="tltitle">Shipment SHP001 (Hindalco)</div><div class="tlmeta"><span style="color:var(--danger)">Predicted Cost: ₹4.2L</span><span>Demurrage & SLA Penalty</span></div></div></div>
            
            <div class="tli"><div class="tldot" style="background:var(--warning)"></div>
            <div><div class="tltitle">JNPT Container Hold</div><div class="tlmeta"><span style="color:var(--warning)">Predicted Cost: ₹1.8L</span><span>Warehousing surge fees</span></div></div></div>
            
            <div class="tli"><div class="tldot" style="background:var(--info)"></div>
            <div><div class="tltitle">Wipro IT Hardware Transit</div><div class="tlmeta"><span style="color:var(--info)">Protected</span><span>In-built grace period</span></div></div></div>
          </div>
          
          <div class="ct" style="font-size:12.5px;margin:18px 0 12px">Predicted Carrier Delay Costs</div>
          <div style="position: relative; height: 160px; width: 100%;"><canvas id="costDelayChart"></canvas></div>
        </div>
      </div>
    </div>

    <!-- API INTEGRATION -->
    <div class="page" id="page-integrations">
      <div class="alert" style="border-left:4px solid var(--accent2)">
        <strong>PROFESSIONAL FEATURE:</strong> API Integration Hub is active. Securely connect your supply chain architecture.
      </div>
      <div class="g3">
        <!-- ERP -->
        <div class="card">
          <div class="ch" style="margin-bottom:10px">
            <div class="ct">ERP Systems Integration</div>
            <span class="nbadge" style="background:var(--success);color:#fff">Active</span>
          </div>
          <div style="font-size:12px;color:var(--text-dim);margin-bottom:20px;line-height:1.5">Connect enterprise resource planners to auto-ingest POs, contract values, and inventory levels.</div>
          
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;padding:12px;background:var(--surface2);border-radius:8px">
            <div style="width:40px;height:40px;background:#fff;border-radius:6px;display:flex;align-items:center;justify-content:center"><img src="https://upload.wikimedia.org/wikipedia/commons/5/59/SAP_2011_logo.svg" width="24" height="12" alt="SAP"></div>
            <div><div style="font-size:13px;font-weight:600">SAP S/4HANA</div><div style="font-size:11px;color:var(--success)">Connected (Synced 2m ago)</div></div>
          </div>
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;padding:12px;background:var(--surface2);border-radius:8px">
            <div style="width:40px;height:40px;background:#fff;border-radius:6px;display:flex;align-items:center;justify-content:center"><img src="https://upload.wikimedia.org/wikipedia/commons/5/50/Oracle_logo.svg" width="28" height="8" alt="Oracle"></div>
            <div><div style="font-size:13px;font-weight:600">Oracle NetSuite</div><div style="font-size:11px;color:var(--text-dim)">Ready to connect</div></div>
            <button class="btn" style="margin-left:auto;padding:5px 12px;font-size:11px">Connect</button>
          </div>
        </div>
        
        <!-- LOGISTICS -->
        <div class="card">
          <div class="ch" style="margin-bottom:10px">
            <div class="ct">Logistics Systems API</div>
            <span class="nbadge" style="background:var(--accent2);color:#fff">Configured</span>
          </div>
          <div style="font-size:12px;color:var(--text-dim);margin-bottom:20px;line-height:1.5">Stream live GPS pings, freight forwarding telemetry, and port authority data directly.</div>
          
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;padding:12px;background:var(--surface2);border-radius:8px">
            <div style="width:40px;height:40px;background:#323232;border-radius:6px;display:flex;align-items:center;justify-content:center"><div style="font-weight:700;color:#fff;font-size:10px">PROJECT44</div></div>
            <div><div style="font-size:13px;font-weight:600">Project44 Telemetry</div><div style="font-size:11px;color:var(--success)">Webhooks Active</div></div>
          </div>
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;padding:12px;background:var(--surface2);border-radius:8px">
            <div style="width:40px;height:40px;background:#fff;border-radius:6px;display:flex;align-items:center;justify-content:center;color:#000;font-weight:bold;font-size:10px">FLEXPORT</div>
            <div><div style="font-size:13px;font-weight:600">Flexport API</div><div style="font-size:11px;color:var(--success)">Ocean Freight tracking synced</div></div>
          </div>
        </div>
        
        <!-- EXCEL -->
        <div class="card">
          <div class="ch" style="margin-bottom:10px">
            <div class="ct">Manual Excel Uploads</div>
          </div>
          <div style="font-size:12px;color:var(--text-dim);margin-bottom:20px;line-height:1.5">Need to manually process vendor lists or legacy contracts? Drop your Excel sheets here.</div>
          
          <div style="border:2px dashed var(--border2);border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;height:120px;background:rgba(255,255,255,0.01);cursor:pointer;transition:all 0.2s">
            <div style="font-size:24px;margin-bottom:8px">📄</div>
            <div style="font-size:12px;color:var(--text-muted)">Drag & drop .XLSX or .CSV here</div>
          </div>
          
          <div style="margin-top:16px;text-align:center">
             <button class="btn" style="width:100%">Browse Local Files</button>
          </div>
        </div>
      </div>
    </div>

    <!-- AUTOMATED REPORTS -->
    <div class="page" id="page-reports">
      <div class="g46">
        <div class="card">
           <div class="ch"><div class="ct">Generate & Export PDF Reports</div></div>
           <p style="font-size:13px;color:var(--text-dim);margin-bottom:20px">Generate executive-ready PDF folios summarizing supply chain friction, current value-at-risk, and AI-driven mitigation recommendations.</p>
           
           <div class="fgrid">
              <div class="fg">
                <label class="fl">Report Template</label>
                <select class="ai-input">
                  <option>Executive Risk Summary</option>
                  <option>Supplier Audit (Deep-Dive)</option>
                  <option>Financial Impact & Loss Estimation</option>
                </select>
              </div>
              <div class="fg">
                <label class="fl">Time Filter</label>
                <select class="ai-input">
                  <option>Last 30 Days</option>
                  <option>Last 90 Days</option>
                  <option>Year To Date</option>
                </select>
              </div>
           </div>
           
           <button class="btn" style="margin-top:20px;background:var(--surface2);border:1px solid var(--border);width:100%" onclick="alert('Generating 14-page PDF document. Please wait...')">📄 Download PDF Report</button>
        </div>
        
        <div class="card">
           <div class="ch"><div class="ct">Automated Report Scheduling</div></div>
           
           <div style="display:flex; justify-content:space-between; align-items:center; padding:16px; background:var(--surface2); border-radius:10px; margin-bottom:12px">
             <div>
               <div style="font-weight:600;font-size:14px;color:var(--text);margin-bottom:4px">Weekly Risk Reports</div>
               <div style="font-size:11px;color:var(--text-muted)">Sent every Monday at 8:00 AM IST</div>
             </div>
             <div>
               <label style="position:relative;display:inline-block;width:40px;height:24px"><input type="checkbox" checked style="opacity:0;width:0;height:0"><span style="position:absolute;cursor:pointer;top:0;left:0;right:0;bottom:0;background-color:var(--accent);transition:.4s;border-radius:34px"></span><span style="position:absolute;content:'';height:16px;width:16px;left:4px;bottom:4px;background-color:white;transition:.4s;border-radius:50%;transform:translateX(16px)"></span></label>
             </div>
           </div>
           
           <div style="display:flex; justify-content:space-between; align-items:center; padding:16px; background:var(--surface2); border-radius:10px;">
             <div>
               <div style="font-weight:600;font-size:14px;color:var(--text);margin-bottom:4px">Monthly Executive Analysis</div>
               <div style="font-size:11px;color:var(--text-muted)">Dispatched on 1st of every month to Management</div>
             </div>
             <div>
               <label style="position:relative;display:inline-block;width:40px;height:24px"><input type="checkbox" checked style="opacity:0;width:0;height:0"><span style="position:absolute;cursor:pointer;top:0;left:0;right:0;bottom:0;background-color:var(--accent);transition:.4s;border-radius:34px"></span><span style="position:absolute;content:'';height:16px;width:16px;left:4px;bottom:4px;background-color:white;transition:.4s;border-radius:50%;transform:translateX(16px)"></span></label>
             </div>
           </div>
           
           <div class="fg" style="margin-top:20px">
              <label class="fl">Subscribed Distribution List</label>
              <input type="text" class="ai-input" value="cxo_board@chainguard.in, vp_procurement@chainguard.in">
           </div>
        </div>
      </div>
    </div>

    <!-- HISTORICAL RISK ANALYTICS -->
    <div class="page" id="page-history">
      <div class="card" style="margin-bottom:18px">
        <div class="ch">
           <div>
             <div class="ct">Long-Term Historical Risk Trends</div>
             <div class="csub">Analyzed rolling behavior across multi-year architectures</div>
           </div>
           <div style="display:flex;gap:7px"><span class="fb active">1-Year</span><span class="fb">3-Year</span></div>
        </div>
        <div style="position: relative; height: 180px; width: 100%;"><canvas id="histTrendChart"></canvas></div>
      </div>
      
      <div class="g2">
        <div class="card">
          <div class="ch"><div class="ct">Monthly Disruption Analysis</div></div>
          <div style="position: relative; height: 220px; width: 100%;"><canvas id="histMonthlyChart"></canvas></div>
        </div>
        
        <div class="card">
          <div class="ch">
            <div>
              <div class="ct">Supplier Benchmarking & Comparison</div>
              <div class="csub">Compare vendor resilience historically side-by-side</div>
            </div>
          </div>
          <div style="display:flex;gap:12px;margin-bottom:12px">
            <select class="ai-input" style="flex:1" onchange="loadHistory()"><option>Hindalco Industries (SUP1025)</option><option>Asian Paints Supply</option></select>
            <span style="color:var(--text-muted);font-weight:bold;margin-top:8px">VS</span>
            <select class="ai-input" style="flex:1" onchange="loadHistory()"><option>Tata Steel Ltd (SUP1000)</option><option>JSW Steel</option></select>
          </div>
          <div style="position: relative; height: 155px; width: 100%;"><canvas id="histCompareChart"></canvas></div>
        </div>
      </div>
    </div>
"""
if 'id="page-cost"' not in text:
    text = text.replace("    <!-- ANALYTICS -->", pages_to_inject + "\n    <!-- ANALYTICS -->")

# 5. JS CHARTS INJECTION
js_load_fns = """
    function loadCost() {
      if(!ch['costLoss']) {
        const c1 = document.getElementById('costLossChart').getContext('2d');
        ch['costLoss'] = new Chart(c1, {
          type: 'bar', data: { labels: ['Electronics', 'Auto', 'Energy', 'Raw Materials'], datasets: [{ data: [45.2, 38.6, 28.1, 30.6], backgroundColor: 'rgba(239, 68, 68, 0.7)', borderRadius: 4 }] },
          options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { y: { ticks: { callback: v => `₹${v}L` } } } }
        });
        
        const c2 = document.getElementById('costDelayChart').getContext('2d');
        ch['costDelay'] = new Chart(c2, {
          type: 'doughnut', data: { labels: ['Demurrage', 'Warehousing', 'Late Penalties', 'Expedited Air Freight'], datasets: [{ data: [8.5, 4.2, 3.1, 2.4], backgroundColor: ['#EF4444', '#F59E0B', '#38BDF8', '#8B5CF6'], borderWidth: 0 }] },
          options: { responsive: true, maintainAspectRatio: false, cutout: '65%', plugins: { legend: { position: 'right', labels: { boxWidth: 10, color: '#7A8BA8' } } } }
        });
      }
    }
    
    function loadIntegrations() { }
    function loadReports() { }
    
    function loadHistory() {
      if(!ch['histTrend']) {
        const ctx1 = document.getElementById('histTrendChart').getContext('2d');
        const months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
        ch['histTrend'] = new Chart(ctx1, {
          type: 'line', data: { labels: months, datasets: [
             { label:'2025 Risk Base', data:[35,33,36,41,45,42,40,38,36,44,48,45], borderColor:'rgba(255,255,255,0.2)', borderWidth:2, borderDash:[5,5], pointRadius:0 },
             { label:'2026 Forecasted & Realized', data:[34,31,48,51,55,50,49,45,41,52,58,54], borderColor:'#6366F1', backgroundColor:'rgba(99,102,241,0.1)', borderWidth:3, fill:true, pointRadius:4 }
          ]},
          options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { labels: { color: '#7A8BA8' } } }, scales: { y: { min: 20 } } }
        });
      }
      
      if(!ch['histMonthly']) {
        const ctx2 = document.getElementById('histMonthlyChart').getContext('2d');
        ch['histMonthly'] = new Chart(ctx2, {
          type: 'bar', data: { labels: ['Jan','Feb','Mar','Apr','May','Jun'], datasets: [{ label: 'Incidents Configured', data: [12,9,18,15,22,11], backgroundColor: 'rgba(56, 189, 248, 0.6)' }] },
          options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } } }
        });
      }
      
      if(ch['histCompare']) {
        // Redraw random data on select change for visual interactivity 
        ch['histCompare'].data.datasets[0].data = [Math.random()*20+5, Math.random()*15+4, Math.random()*25+10, Math.random()*20+5, Math.random()*10+5, Math.random()*15+5];
        ch['histCompare'].data.datasets[1].data = [Math.random()*10+2, Math.random()*10+2, Math.random()*8+2, Math.random()*10+3, Math.random()*5+1, Math.random()*7+2];
        ch['histCompare'].update();
      } else {
        const ctx3 = document.getElementById('histCompareChart').getContext('2d');
        ch['histCompare'] = new Chart(ctx3, {
          type: 'radar', data: { 
            labels: ['Price Fluctuations', 'Quality Drops', 'Delivery Delays', 'Geopolitics', 'Financial Stress', 'ESG Lapses'],
            datasets: [
               { label: 'Supplier A', data: [15,8,22,12,6,10], backgroundColor: 'rgba(239, 68, 68, 0.2)', borderColor: '#EF4444', borderWidth:2 },
               { label: 'Supplier B', data: [7,4,6,8,2,4], backgroundColor: 'rgba(34, 197, 94, 0.2)', borderColor: '#22C55E', borderWidth:2 }
            ]
          },
          options: { responsive: true, maintainAspectRatio: false, scales: { r: { ticks: { display: false }, grid: { color: 'rgba(255,255,255,0.05)' } } }, plugins: { legend: { display: false } } }
        });
      }
    }
"""
if "function loadCost()" not in text:
    text = text.replace("// ── ANALYTICS ──", js_load_fns + "\n    // ── ANALYTICS ──")

with codecs.open(html_path, 'w', 'utf-8') as f:
    f.write(text)

print("Injected UI Pages and Scripts Successfully!")
