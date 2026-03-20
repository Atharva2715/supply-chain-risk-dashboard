import os

html_path = 'c:/Users/Atharva/OneDrive/Desktop/supply chain risk/chainguard_demo.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Inject Navigation Item
nav_inject = """      <div class="nav-item" onclick="nav('predict',this)"><span class="nav-icon">◎</span>ML Predictor</div>
      <div class="nav-item" onclick="nav('scenario',this)"><span class="nav-icon">⚄</span>Scenario Engine</div>"""

if '<div class="nav-item" onclick="nav(\'scenario\',this)">' not in text:
    text = text.replace(
        """      <div class="nav-item" onclick="nav('predict',this)"><span class="nav-icon">◎</span>ML Predictor</div>""",
        nav_inject
    )

    # 2. Add scenario to nav mapping
    text = text.replace(
        "predict: 'ML Risk Predictor', analytics: 'Analytics & Insights', tracker: '📍 Real-Time Location Tracker' };",
        "predict: 'ML Risk Predictor', scenario: 'What-If Cost Simulation', analytics: 'Analytics & Insights', tracker: '📍 Real-Time Location Tracker' };"
    )
    
    # 3. Add to load triggers
    text = text.replace(
        "if (page === 'predict') loadPredict();",
        "if (page === 'predict') loadPredict();\n      if (page === 'scenario') loadScenario();"
    )

# 4. Inject the HTML Page for Scenario Engine before page-analytics
scenario_html = """
    <!-- SCENARIO ENGINE -->
    <div class="page" id="page-scenario">
      <div class="g46" style="align-items:start">
        <!-- What-If Control Panel -->
        <div class="card">
          <div class="ch">
            <div>
              <div class="ct">What-If Simulation Engine</div>
              <div class="csub">Simulate macro-economic shocks & supply chain strains</div>
            </div>
          </div>
          
          <div class="fgrid">
            <div class="fg"><label class="fl">Fuel & Energy Costs (+%)</label>
              <div class="sr"><input type="range" min="0" max="100" step="5" value="0" id="sim1" oninput="sv('simV1',this.value)"><span class="sv" id="simV1">0</span></div>
            </div>
            <div class="fg"><label class="fl">Global Tariff Rate (+%)</label>
              <div class="sr"><input type="range" min="0" max="50" step="1" value="0" id="sim2" oninput="sv('simV2',this.value)"><span class="sv" id="simV2">0</span></div>
            </div>
            <div class="fg"><label class="fl">Labor Unrest Probability</label>
              <div class="sr"><input type="range" min="0" max="1" step="0.05" value="0.1" id="sim3" oninput="sv('simV3',this.value)"><span class="sv" id="simV3">0.10</span></div>
            </div>
            <div class="fg"><label class="fl">Port Congestion Delay (Days)</label>
              <div class="sr"><input type="range" min="0" max="30" step="1" value="3" id="sim4" oninput="sv('simV4',this.value)"><span class="sv" id="simV4">3</span></div>
            </div>
          </div>
          
          <div style="margin-top:20px;display:flex;gap:12px;align-items:center">
            <button class="btn" onclick="runSimulation()" style="background:linear-gradient(135deg, #F59E0B, #EA580C)">⚡ Run Scenario Simulation</button>
          </div>
          
          <!-- Auto Decision Recommendation Output -->
          <div class="pres" id="simDecisions" style="margin-top:20px; border-color:rgba(234,88,12,0.3); background:rgba(234,88,12,0.05)">
            <div class="sec" style="color:#F59E0B">Auto Decision Recommendations</div>
            <ul style="font-size:12px; padding-left:16px; margin-top:10px; line-height:1.6; color:var(--text-muted)" id="simRecList">
              <li>Awaiting simulation execution...</li>
            </ul>
          </div>
        </div>
        
        <!-- Cost Impact Prediction Dashboard -->
        <div class="card">
          <div class="ch">
            <div>
              <div class="ct">Cost Impact Prediction</div>
              <div class="csub">Financial exposure modeling based on scenario</div>
            </div>
          </div>
          
          <div class="stats" style="grid-template-columns: 1fr 1fr; margin-bottom:18px;">
            <div class="scard d" style="padding:14px;">
              <div class="slabel">Projected Financial Loss</div>
              <div class="sval" id="simLoss">₹0.0L</div>
              <div class="ssub" id="simPct">+0.0% vs Baseline</div>
            </div>
            <div class="scard i" style="padding:14px;">
              <div class="slabel">Supplier Failure Count</div>
              <div class="sval" id="simFail">0</div>
              <div class="ssub">Simulated bankruptcies/defaults</div>
            </div>
          </div>
          
          <div class="ct" style="font-size:12.5px;margin-bottom:12px">Impact by Industry Category</div>
          <div style="position: relative; height: 180px; width: 100%;"><canvas id="simImpactChart"></canvas></div>
        </div>
      </div>
    </div>
"""

if 'id="page-scenario"' not in text:
    text = text.replace(
        "    <!-- ANALYTICS -->",
        scenario_html + "\n    <!-- ANALYTICS -->"
    )

# 5. Inject Javascript Implementation Logic
scenario_js = """
    // ── SCENARIO ENGINE LOGIC ──
    function loadScenario() {
      // Just initialize empty charts if they don't exist
      if(!ch['simImpact']) {
        const ctx = document.getElementById('simImpactChart').getContext('2d');
        ch['simImpact'] = new Chart(ctx, {
          type: 'bar', 
          data: { 
            labels: ['Electronics', 'Energy', 'Pharma', 'Agri-Products', 'Logistics'], 
            datasets: [{ 
              data: [0,0,0,0,0], 
              backgroundColor: 'rgba(234,88,12,0.6)', 
              borderColor: '#EA580C', 
              borderWidth: 1, 
              borderRadius: 4 
            }] 
          },
          options: { 
            responsive: true, 
            maintainAspectRatio: false, 
            plugins: { legend: { display: false }, tooltip: { callbacks: { label: c => `₹${c.raw}L` } } }, 
            scales: { x: { grid: { display: false } }, y: { beginAtZero: true } } 
          }
        });
      }
    }

    function runSimulation() {
      const fuel = parseFloat(document.getElementById('sim1').value);
      const tariff = parseFloat(document.getElementById('sim2').value);
      const lab = parseFloat(document.getElementById('sim3').value);
      const port = parseFloat(document.getElementById('sim4').value);
      
      // Compute mathematical simulation logic mapping constraints
      // Cost Impact Prediction
      const baseLoss = 24.5; // 24.5L base
      const multiplier = 1 + (fuel/100)*0.4 + (tariff/100)*0.6 + lab*0.8 + (port/30)*0.5;
      const totalLoss = baseLoss * multiplier;
      
      const pctIncrease = ((multiplier - 1) * 100).toFixed(1);
      const failureCount = Math.floor(multiplier * 1.5 + (Math.random()*2));
      
      // Update Cost Impact Numbers
      document.getElementById('simLoss').textContent = `₹${totalLoss.toFixed(1)}L`;
      document.getElementById('simPct').textContent = `+${pctIncrease}% vs Baseline`;
      document.getElementById('simFail').textContent = failureCount;
      
      // Animate Chart Update
      const simData = [
         (fuel * 0.5 + tariff * 0.8) * 1.2,
         (fuel * 1.2 + tariff * 0.1),
         (port * 1.5 + lab * 10),
         (tariff * 0.8 + lab * 5),
         (fuel * 1.5 + port * 2)
      ].map(v => Math.floor(v + 5));
      
      ch['simImpact'].data.datasets[0].data = simData;
      ch['simImpact'].update();
      
      // Generate Auto Decision Recommendations based on inputs
      const recList = document.getElementById('simRecList');
      let recs = [];
      
      if(fuel > 40) recs.push("<strong>Fuel cost extreme:</strong> Shift 45% of trucking logistics to rail freight immediately to absorb margin compression.");
      if(tariff > 20) recs.push("<strong>Tariff barrier detected:</strong> Activate dual-sourcing protocol. Move procurement from West Bengal to localized Maharashtra suppliers.");
      if(lab > 0.5) recs.push("<strong>High labor unrest:</strong> Pre-approve overtime budgets for unaffected regional plants. Increase safety stock by 20% globally.");
      if(port > 10) recs.push("<strong>Severe port timeline:</strong> Reroute maritime containers to Gujarat JNPT port and fallback to air-freight for Critical priority items.");
      
      if(recs.length === 0) recs.push("Macro environment stable. Maintain standard procurement operations and Just-in-Time inventory models.");
      
      recList.innerHTML = recs.map(r => `<li style="margin-bottom:8px">${r}</li>`).join('');
      
      // Show container
      const decBox = document.getElementById('simDecisions');
      decBox.classList.add('show');
    }
"""

if '// ── SCENARIO ENGINE LOGIC ──' not in text:
    text = text.replace(
        "// ── ANALYTICS ──",
        scenario_js + "\n    // ── ANALYTICS ──"
    )

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Injected Scenario Simulation Engine Successfully!")
