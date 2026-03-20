import re

def fix():
    with open('c:/Users/Atharva/OneDrive/Desktop/supply chain risk/chainguard_demo.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace <canvas id="xyz" height="90"></canvas> with the proper wrapped div
    # so that Chart.js does not fall into the endless shrink loop
    pattern = r'<canvas\s+id=[\'\"]([^\'\"]+)[\'\"](?:([^>]*)height=[\'\"]([0-9]+)[\'\"]([^>]*)|([^>]*))>.*?</canvas>'
    
    def repl(m):
        id_val = m.group(1)
        h_val = m.group(3)
        rest1 = m.group(2) if m.group(2) else ""
        rest2 = m.group(4) if m.group(4) else ""
        rest3 = m.group(5) if m.group(5) else ""
        all_rest = rest1 + rest2 + rest3
        
        if h_val:
            return f'<div style=\"position: relative; height: {h_val}px; width: 100%;\"><canvas id=\"{id_val}\" {all_rest}></canvas></div>'
        else:
            return f'<div style=\"position: relative; height: 100%; width: 100%;\"><canvas id=\"{id_val}\" {all_rest}></canvas></div>'

    new_html = re.sub(pattern, repl, html)

    with open('c:/Users/Atharva/OneDrive/Desktop/supply chain risk/chainguard_demo.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

fix()
print("Canvas wrapped correctly to fix shrink loop.")
