import re

html_path = 'c:/Users/Atharva/OneDrive/Desktop/supply chain risk/chainguard_demo.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Make sure we don't double wrap
if '<div style="position: relative; height:' not in text:
    pattern = re.compile(r'<canvas\s+id=[\'\"]([a-zA-Z0-9_]+)[\'\"](?:\s+height=[\'\"]([0-9]+)[\'\"])?\s*></canvas>')
    
    def repl(m):
        cid = m.group(1)
        h = m.group(2)
        if h:
            return f'<div style="position: relative; height: {h}px; width: 100%;"><canvas id="{cid}"></canvas></div>'
        else:
            return f'<div style="position: relative; height: 100%; width: 100%;"><canvas id="{cid}"></canvas></div>'

    new_text = pattern.sub(repl, text)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Wrapped successfully.")
else:
    print("Already wrapped.")
