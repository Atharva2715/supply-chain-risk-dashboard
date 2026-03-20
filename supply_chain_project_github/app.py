import os
import sys
import random
import threading
import webbrowser
from flask import Flask, send_file, request, jsonify

# Automatically switch to the script's directory so it finds the html file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/')
def home():
    # Serve the high-end dashboard HTML provided by user exactly as requested
    # Reading manually prevents aggresive static file caching.
    with open('chainguard_demo.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    return html_content

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    r = data.get('r', 0.5)
    f = data.get('f', 0.5)
    g = data.get('g', 0.5)
    d = data.get('d', 0.5)
    q = data.get('q', 0.5)
    y = data.get('y', 2)
    
    # Core mathematical risk model integration
    rs = (1-r)*0.25 + (1-f)*0.30 + g*0.20 + (1-d)*0.15 + (1-q)*0.10
    fp = min(0.99, rs*1.8 + (1 - y/30)*0.05 + random.uniform(0, 0.05))
    
    if rs > 0.45: level = 'Critical'
    elif rs > 0.30: level = 'High'
    elif rs > 0.15: level = 'Medium'
    else: level = 'Low'
    
    recs = {
        'Critical': 'URGENT: Immediately activate backup suppliers. Initiate contingency procurement. Schedule emergency review meeting.',
        'High': 'High priority: Diversify supplier base, increase safety stock levels, and conduct monthly performance reviews.',
        'Medium': 'Monitor closely: Set up automated alerts, review contract terms, and assess alternative suppliers.',
        'Low': 'Maintain standard monitoring protocols. Schedule quarterly reviews and update risk assessments.'
    }
    
    return jsonify({
        'fp': fp,
        'rs': rs,
        'level': level,
        'rec': recs[level]
    })

@app.route('/ask_ai', methods=['POST'])
def ask_ai():
    data = request.json
    q = data.get('query', '').lower()
    
    # Mocking a generative AI reasoning engine
    import time
    time.sleep(1.5) # Simulate AI thinking delay
    
    if 'sup1025' in q or 'mitigation draft' in q or 'draft' in q:
        ans = "<strong>Draft Mitigation Email:</strong><br><br>Subject: URGENT - Disruption Contingency Protocol<br>To: Procurement Team<br><br>Due to the critical 94.0% failure probability logged for SUP1025, please immediately execute contingent order #C-9042 with our backup supplier in Gujarat. <br><br>Shall I execute the API call to send this?"
    elif 'fuel' in q or 'scenario' in q or 'what if' in q:
        ans = "<strong>Scenario Analysis: Fuel +20%</strong><br><br>Running Monte Carlo simulation across your live network...<br><br>• Global transit costs will rise by 8.4%.<br>• Logistics Risk Index will transition from <strong>Medium</strong> to <strong style='color:var(--danger)'>Critical</strong>.<br>• Recommended action: Consolidate smaller shipment batches and utilize rail freight where possible."
    elif 'highest risk' in q or 'top' in q or 'summary' in q:
        ans = "Based on current telemetry, the top 3 highest-risk suppliers right now are:<br><br>1. <strong>Hindalco Industries</strong> (94.0% - Transport Delay)<br>2. <strong>Maruti Vendors</strong> (51.0% - Strike Alert)<br>3. <strong>Asian Paints Supply</strong> (43.9% - Weather Anomaly)<br><br>Would you like to initiate standard mitigation protocols for these?"
    else:
        ans = "I've analyzed the knowledge graph of your supply chain network against real-time global telemetry. <br><br>Based on recent patterns, my predictive model recommends increasing safety stock across all Auto Component categories by 15% due to incoming port congestion warnings in West Bengal."
        
    return jsonify({'answer': ans})

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    # Wait one second to ensure the Flask server has fully started before popping the browser tab
    threading.Timer(1.0, open_browser).start()
    app.run(host="0.0.0.0", port=5000, debug=False)
